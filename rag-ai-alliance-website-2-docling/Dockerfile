FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 


# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    git \
    wget \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# gcc \

# Copy requirements file
COPY requirements-docker.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements-docker.txt

# Copy project files
COPY . .

# Create a non-root user and switch to it
RUN adduser --disabled-password --gecos '' appuser
RUN chown -R appuser:appuser /app
USER appuser

# Expose the port the app runs on
EXPOSE 5000

# flask application
# ENV FLASK_APP=app.py 
# ENV FLASK_ENV=development
# ENV FLASK_DEBUG=1
# ## Run the application using flask run
# CMD ["flask", "run", "--host=0.0.0.0", "--no-debugger", "--no-reload"]

CMD ["python", "app.py"]
