from get_tool_via_llm import ask_llm, call_tool, parse_tool_call
from prompts import system_prompt
from toolkit import get_file_content
import os
import json
from dotenv import load_dotenv
load_dotenv()


MAX_STEPS = 20

def classify_intent(user_input: str) -> str:
    text = user_input.lower()

    if any(k in text for k in ["update", "change", "modify", "fix", "refactor"]):
        return "code_edit"

    if any(k in text for k in ["explain", "how", "what does", "describe"]):
        return "code_read"

    return "unknown"

def run_agent(user_input, working_directory="calculator"):
    intent = classify_intent(user_input)

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_input},
    ]

    # Controller-forced exploration
    TARGET_FILES = ["pkg/calculator.py", "main.py"]
    if intent in ("code_edit", "code_read"):
        for file in TARGET_FILES:
            content = get_file_content(working_directory, file)
            messages.append({"role": "tool", "content": f"{file}\n{content}"})

    for step in range(3):  # small, deterministic
        llm_output = ask_llm(messages)

        tool_name, args = parse_tool_call(llm_output)

        if tool_name is None:
            continue

        if tool_name == "none":
            return llm_output

        result = call_tool(tool_name, args, working_directory, intent)

        messages.append({"role": "assistant", "content": llm_output})
        messages.append({"role": "tool", "content": result, "tool_call_id": tool_name})

        if intent == "code_edit":
            return

    return "Agent stopped after 3 steps."
