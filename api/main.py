from fastapi import FastAPI
from uuid import uuid4
import threading
import os
import json

app = FastAPI()

sessions = {}
user_questions = []

@app.post("/chat/")
async def buora(input_string: dict):
    previous_messages = input_string.get("messages")

    return {"answer": "resposta aqui!"}