from fastapi import FastAPI, Form, HTTPException
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
import concurrent.futures
import asyncio  # Add this import
import ollama

app = FastAPI()

# Serve static files (e.g., CSS, JS, images)
app.mount("/static", StaticFiles(directory="static"), name="static")

def chat_with_ollama(question):
    try:
        return ollama.chat(model='llama2', messages=[{'role': 'user', 'content': question, },])
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error in Ollama API: {str(e)}")

@app.get("/", response_class=HTMLResponse)
async def read_root():
    return FileResponse("static/index.html")

@app.post("/get_answer")
async def get_answer(question: str = Form(...)):
    try:
        # Use ThreadPoolExecutor for parallel requests
        with concurrent.futures.ThreadPoolExecutor() as executor:
            # Make parallel requests to Ollama using submit
            loop = asyncio.get_event_loop()
            responses = await loop.run_in_executor(executor, lambda: [chat_with_ollama(question) for _ in range(1)])

        # Process the responses as needed
        result = {"responses": []}
        for response in responses:
            result["responses"].append(response['message']['content'] if 'message' in response and 'content' in response['message'] else "No response")

        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")
