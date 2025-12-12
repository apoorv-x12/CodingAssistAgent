# functions/run_python_file.py

import os
import subprocess

def run_python_file(working_directory, file_path, args=[]):
    try:
        base = os.path.abspath(working_directory)
        target = os.path.abspath(os.path.join(working_directory, file_path))

        # Guardrail: path must stay inside working_directory
        if not target.startswith(base):
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

        # Must exist
        if not os.path.exists(target):
            return f'Error: File "{file_path}" not found.'

        # Must be a python file
        if not file_path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file.'

        # Build command
        cmd = ["python", target] + args

        # Run the subprocess
        result = subprocess.run(
            cmd,
            cwd=base,
            capture_output=True,
            text=True,
            timeout=30
        )

        stdout = result.stdout.strip()
        stderr = result.stderr.strip()

        output_parts = []

        if stdout:
            output_parts.append(f"STDOUT:\n{stdout}")
        if stderr:
            output_parts.append(f"STDERR:\n{stderr}")
        if result.returncode != 0:
            output_parts.append(f"Process exited with code {result.returncode}")
        if not output_parts:
            return "No output produced"

        return "\n".join(output_parts)

    except Exception as e:
        return f"Error: executing Python file: {e}"
