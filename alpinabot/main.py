import os
from fastapi import FastAPI
from pydantic import BaseModel
from openai import OpenAI


app = FastAPI()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


class ChatRequest(BaseModel):
    message: str


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/chat")
def chat(req: ChatRequest):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": req.message}
        ]
    )
    return {
        "response": response.choices[0].message.content
    }
