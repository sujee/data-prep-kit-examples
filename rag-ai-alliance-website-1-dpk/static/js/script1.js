document.addEventListener('DOMContentLoaded', () => {
    const chatForm = document.getElementById('chatForm');
    const userInput = document.getElementById('userInput');
    const chatMessages = document.getElementById('chatMessages');

    chatForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        
        const message = userInput.value.trim();
        if (!message) return;
        
        // Add user message to chat
        addMessage(message, 'user');
        userInput.value = '';
        
        // Add loading indicator
        const loadingDiv = document.createElement('div');
        loadingDiv.className = 'message system loading';
        loadingDiv.innerHTML = '<div class="spinner"></div><div>Thinking...</div>';
        chatMessages.appendChild(loadingDiv);
        chatMessages.scrollTop = chatMessages.scrollHeight;
        
        try {
            // Send message to server
            const response = await fetch('/chat', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    message: message
                })
            });
            
            const data = await response.json();
            
            // Remove loading indicator
            chatMessages.removeChild(loadingDiv);
            
            // Add system response
            addMessage(data.response, 'system');
            
        } catch (error) {
            console.error('Error:', error);
            chatMessages.removeChild(loadingDiv);
            addMessage('Sorry, something went wrong. Please try again.', 'system');
        }
    });

    function addMessage(text, sender) {
        const messageDiv = document.createElement('div');
        messageDiv.className = `message ${sender}`;
        messageDiv.textContent = text;
        
        chatMessages.appendChild(messageDiv);
        chatMessages.scrollTop = chatMessages.scrollHeight;
    }
});
