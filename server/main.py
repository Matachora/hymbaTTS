from fastapi import FastAPI, File, UploadFile, Response
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["http://localhost:5500", "http://127.0.0.1:5500"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"], 
)

@app.get("/")
async def auth(user_cookie):
    return {"message": "Hello World"}

@app.get("/singup")
async def singup():
    return {"username": "Edwin", "pass": "123"}

@app.get("/audio/{filename}")
async def get_audio(filename: str):
    try:
        with open(f"audios/{filename}.mp3", "rb") as f: 
            audio_data = f.read()
        return Response(content=audio_data, media_type="audio/mpeg") 
    except FileNotFoundError:
        return {"error": "Audio file not found."}, 404