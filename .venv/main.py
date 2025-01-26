from fastapi import FastAPI

import time
import threading

from src.tts import ooola, slow

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/hola")
async def root():
    return {"hola": "mundo"}

@app.get("/items/{item_id}")
async def read_item(item_id: bool):
    return {"item id": item_id}

@app.get("/binding_tests")
async def bind_function():
    a = ooola()
    return{"ooola says:": a}

@app.get("/slow")
async def slowly():
    threading.Thread(target=slow, daemon=False).start()
    return{"VAlor de retorno de slow()": "nada"}