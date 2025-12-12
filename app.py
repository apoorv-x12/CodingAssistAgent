from fastapi import FastAPI
from agent import run_agent
app=FastAPI()

'''
Model	Why
llama-3.1-70b-versatile	Best reasoning, closest to GPT-4, works for everything
llama-3.1-8b-instant	Fastest + very cheap
mixtral-8x7b	Good balanced model
'''
@app.get("/chat")
def chat(q: str):
    
    resp=run_agent(q)
    return {"reply": resp}




