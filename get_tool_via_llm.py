from groq import Groq
from toolkit import TOOLS
import os
import json
from dotenv import load_dotenv
load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def ask_llm(messages):
    resp = client.chat.completions.create(
        model="llama-3.1-70b-versatile",
        messages=messages,
    )
    return resp.choices[0].message.content


def parse_tool_call(text):
    try:
        data = json.loads(text)
        return data.get("tool"), data.get("args", {})
    except json.JSONDecodeError:
        # LLM didn't return JSON — treat the full text as the final assistant response
        # Returning ("none", {}) makes run_agent() return the LLM text to the user.
        return "none", {}
    


def call_tool(tool_name, args, working_directory="calculator"):
    if tool_name not in TOOLS:
        return f"Error: Unknown tool '{tool_name}'"
    fn = TOOLS[tool_name]
    return fn(working_directory, **args)
