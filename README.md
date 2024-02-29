# OllamaFast Chat Application

## Overview

OllamaFast is a simple chat application built with FastAPI and Ollama. It allows users to interact with a chatbot named "mistral" through a WebSocket connection.

## Prerequisites

Before running the application, make sure you have the following installed:

- Python 3.x
- FastAPI
- Ollama
- [Other dependencies]

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/ollamaFast.git
    cd ollamaFast
    ```

2. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Run the FastAPI application:**

    ```bash
    uvicorn main:app --reload
    ```

2. **Open your browser and navigate to [http://127.0.0.1:8000/](http://127.0.0.1:8000/) to access the chat application.**

3. **Interact with the WebSocket at [ws://127.0.0.1:8000/ws](ws://127.0.0.1:8000/ws) using a WebSocket client or integrate it into your own frontend application.**

## Configuration

The application can be configured through environment variables or by modifying the code directly. Key configuration points include:

- **Ollama Chatbot:** The chatbot used is "mistral". You can change this in the `chat_generator` function.

- **Static Files:** The static files (e.g., HTML content) are stored in the "static" directory. Modify the files as needed.

- **WebSocket Endpoint:** The WebSocket endpoint is defined in the `websocket_endpoint` function.

## Contributing

Feel free to contribute by submitting bug reports, feature requests, or pull requests. Your contributions are highly appreciated!

