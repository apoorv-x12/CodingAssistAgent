from get_tool_via_llm import ask_llm, call_tool, parse_tool_call
from prompts import system_prompt
from groq import Groq
import os
import json
from dotenv import load_dotenv
load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

MAX_STEPS = 20

def run_agent(user_input, working_directory="."):

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": f"Working directory: {working_directory}\n\n{user_input}"},
    ]

    for step in range(MAX_STEPS):

        # 1. Ask LLM
        llm_output = ask_llm(messages)

        # 2. Parse tool call
        tool_name, args = parse_tool_call(llm_output)

        # 3. LLM says it's done
        if tool_name == "none" :
            print("Final response:\n" + llm_output)
            return f"Final response:\n{llm_output}"
        
        if tool_name is None:
            print("Error: Could not parse tool call from LLM output.")
            return
        
        # 4. Execute tool
        result = call_tool(tool_name, args, working_directory)

        # 5. Add tool call + tool result to conversation
        messages.append({"role": "assistant", "content": llm_output})
        # Groq chat API requires a `tool_call_id` property on messages with role 'tool'
        # Use the tool name as the tool_call_id so the model can correlate the tool result.
        messages.append({"role": "tool", "content": result, "tool_call_id": tool_name})

    print("Stopped: exceeded max agent steps.")
