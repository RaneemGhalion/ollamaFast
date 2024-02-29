
from ollama import chat


from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import json
import asyncio

app = FastAPI()

class ConnectionManager:
    def __init__(self):
        self.active_connections = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def send_message(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)

manager = ConnectionManager()

app.mount("/static", StaticFiles(directory="static"), name="static")

with open("/home/ranem/ollamaFast/static/index.html", "r") as file:
    html_content = file.read()


@app.get("/", response_class=HTMLResponse)
async def get():
    return HTMLResponse(content=html_content)

async def chat_generator(messages):
    for part in chat('mistral', messages=messages, stream=True):
        yield part['message']['content']
        await asyncio.sleep(0.3)  # Optional: Add a delay between messages

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    
    try:
        while True:
            data = await websocket.receive_text()
            my_dict = json.loads(data)
            
            async for response_content in chat_generator([my_dict]):
                print(response_content)
                await websocket.send_text(response_content)
    except asyncio.CancelledError:
        # Handle disconnection if needed
        pass
    finally:
        manager.disconnect(websocket)
