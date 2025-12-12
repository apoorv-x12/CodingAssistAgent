# functions/write_file.py

import os

def write_file(working_directory, file_path, content):
    try:
        base = os.path.abspath(working_directory)
        target = os.path.abspath(os.path.join(working_directory, file_path))

        # Guardrail: ensure the target is inside working_directory
        if not target.startswith(base):
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

        # Ensure parent directories exist
        parent_dir = os.path.dirname(target)
        if not os.path.exists(parent_dir):
            os.makedirs(parent_dir, exist_ok=True)

        # Write or overwrite file
        with open(target, "w", encoding="utf-8", errors="replace") as f:
            f.write(content)

        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

    except Exception as e:
        return f"Error: {str(e)}"
