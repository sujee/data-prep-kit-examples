import os
import sys
import asyncio
import nest_asyncio

# Disable Streamlit's file watcher for specific modules before importing streamlit
# This prevents the error with torch._classes.__path__._path
os.environ["STREAMLIT_SERVER_WATCH_MODULES"] = "false"

# Apply nest_asyncio to allow nested event loops
nest_asyncio.apply()

# Set up the event loop policy before importing streamlit or torch
if sys.platform == 'win32':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
else:
    asyncio.set_event_loop_policy(asyncio.DefaultEventLoopPolicy())

# Create and set the event loop
loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)

import streamlit as st
from dotenv import dotenv_values, find_dotenv
from my_config import MY_CONFIG
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core import Settings
from llama_index.core import VectorStoreIndex, StorageContext
from llama_index.vector_stores.milvus import MilvusVectorStore
from llama_index.core import VectorStoreIndex
from llama_index.llms.replicate import Replicate


# def run_async(coro):
#     """
#     Helper function to run async code in a synchronous context
#     """
#     loop = asyncio.new_event_loop()
#     asyncio.set_event_loop(loop)
#     result = loop.run_until_complete(coro)
#     loop.close()
#     return result

def run_async(coro):
    """
    Helper function to run async code in a synchronous context
    """
    l = asyncio.get_event_loop()
    if l and l.is_running():
        # Create a new loop for this thread
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        
    loop = asyncio.get_event_loop()
    return loop.run_until_complete(coro)

os.environ['HF_ENDPOINT'] = 'https://hf-mirror.com'


# @st.cache_resource
async def async_initialize():
    import torch

    config = dotenv_values(find_dotenv())
    
    ## ---- init 1: Setup embedding model ---- 
    # print (f"Setting up embedding model : {MY_CONFIG.EMBEDDING_MODEL}")
    st.write (f"Setting up embedding model : {MY_CONFIG.EMBEDDING_MODEL}")
    # st.sidebar.info (f"Setting up embedding model : {MY_CONFIG.EMBEDDING_MODEL}")
    Settings.embed_model = HuggingFaceEmbedding(
        model_name = MY_CONFIG.EMBEDDING_MODEL
    )
    # print (f"✅  embedding model '{MY_CONFIG.EMBEDDING_MODEL}' initialized")
    st.write (f"✅  embedding model '{MY_CONFIG.EMBEDDING_MODEL}' initialized")
    
    ## ---- init 2: connect to Milvus
    # print ('Connecting to vector store: ', MY_CONFIG.DB_URI)
    st.write ('Connecting to vector store: ', MY_CONFIG.DB_URI)
    vector_store = MilvusVectorStore(
        uri = MY_CONFIG.DB_URI ,
        dim = MY_CONFIG.EMBEDDING_LENGTH , 
        collection_name = MY_CONFIG.COLLECTION_NAME,
        overwrite=False  # so we load the index from db
    )
    storage_context = StorageContext.from_defaults(vector_store=vector_store)
    # print ("✅ Connected to Milvus instance: ", MY_CONFIG.DB_URI )
    st.write ("✅ Connected to Milvus instance: ", MY_CONFIG.DB_URI )
    
    ## ---- init 2.5 - load indexed documents

    MY_CONFIG.VECTOR_INDEX = VectorStoreIndex.from_vector_store(
         vector_store=vector_store, storage_context=storage_context)
    # print ("✅ Loaded index from vector db:", MY_CONFIG.DB_URI )
    st.write ("✅ Loaded index from vector db:", MY_CONFIG.DB_URI )

    ## ---- init 3: replicate token ----
    MY_CONFIG.REPLICATE_API_TOKEN = config.get("REPLICATE_API_TOKEN")
    ## Manual override
    # MY_CONFIG.REPLICATE_API_TOKEN="abc123"
    # print ("REPLICATE_API_TOKEN : ", MY_CONFIG.REPLICATE_API_TOKEN )
    if MY_CONFIG.REPLICATE_API_TOKEN:
        # print ('✅ REPLICATE_API_TOKEN found!')
        os.environ["REPLICATE_API_TOKEN"] = MY_CONFIG.REPLICATE_API_TOKEN 
    else:
        raise Exception ("'REPLICATE_API_TOKEN' not found.  Please set it in '.env' file to continue...")

    ## ---- init 4: setup LLM ----
    # print ("Setting up LLM : ", MY_CONFIG.LLM_MODEL)
    st.write ("Setting up LLM : ", MY_CONFIG.LLM_MODEL)
    llm = Replicate(
        model= MY_CONFIG.LLM_MODEL,
        temperature=0.1
    )
    Settings.llm = llm
    # print (f"✅  LLM '{MY_CONFIG.LLM_MODEL}' initialized")
    st.write (f"✅  LLM '{MY_CONFIG.LLM_MODEL}' initialized")
## ----end:   async_initialize  ----------------------

def initialize():
    ## clear chat
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []

    st.write("App initializing ...")
    run_async(async_initialize())
    st.session_state.initialized = True
    st.write("App initialized!")
## --- end: initialize ------------------------
    
async def async_answer_chat(user_input):
    # return f"You said: {user_input}"

    query_engine = MY_CONFIG.VECTOR_INDEX.as_query_engine()
    response = query_engine.query(user_input)
    return response
## --- end: async_answer_chat ------------------------

## -----------------
def answer_chat (user_input):
    response = run_async(async_answer_chat(user_input))
    return response
## -----------------

## ---- streamlit main function -----

st.title(f"👋 Chat with website :  {MY_CONFIG.CRAWL_URL_BASE}")

# # Add a "New Chat" button at the top of the main area
# if st.button("New Chat", type="primary"):
#     st.session_state.chat_history = []
#     st.rerun()

if 'initialized' not in st.session_state:
    result = initialize()
    st.session_state.initialized = True

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []
    
# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("What can I help you with?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.spinner('Finding the answer to your question...'):
        response = answer_chat(prompt)

        # response = f"Echo: {prompt}"  ## DEBUG
        
        # Display assistant response in chat message container
        with st.chat_message("assistant"):
            st.markdown(response)
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})
