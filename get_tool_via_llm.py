from groq import Groq
from toolkit import TOOLS
import os
import json
from dotenv import load_dotenv
load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def ask_llm(messages):
    resp = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=messages,
    )
    return resp.choices[0].message.content


def parse_tool_call(text):
    try:
        data = json.loads(text)
        return data.get("tool"), data.get("args", {})
    except json.JSONDecodeError:
        return None, {}


def call_tool(tool_name, args, working_directory="calculator", intent="unknown"):
    if tool_name not in TOOLS:
        return f"Error: Unknown tool '{tool_name}'"
    
    # Restrict tools by intent
    if intent == "code_read" and tool_name in ["replace_in_file", "write_file"]:
        return f"Error: Tool '{tool_name}' not allowed for read-only intent"
    if intent == "code_edit" and tool_name == "run_python_file":
        return f"Error: Tool '{tool_name}' not allowed for edit intent"
    
    fn = TOOLS[tool_name]
    return fn(working_directory, **args)
