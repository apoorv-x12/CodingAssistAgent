from groq import Groq
from dotenv import load_dotenv
from fastapi import FastAPI
from prompts import system_prompt
import os

app=FastAPI()
load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))
'''
Model	Why
llama-3.1-70b-versatile	Best reasoning, closest to GPT-4, works for everything
llama-3.1-8b-instant	Fastest + very cheap
mixtral-8x7b	Good balanced model
'''

@app.get("/chat")
def chat(q: str):
    resp = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
           # {"role": "system", "content": system_prompt},
            {"role": "user", "content": q}
            ]
    )
    return {"reply": resp.choices[0].message.content}




