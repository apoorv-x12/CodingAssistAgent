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
def chat(q: str,working_directory: str="calculator"):
    
    resp=run_agent(q, working_directory)
    return {"reply": resp}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
