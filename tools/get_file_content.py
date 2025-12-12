# functions/get_file_content.py

import os

MAX_CHARS = 10000  # you can later move this to config.py

def get_file_content(working_directory, file_path):
    try:
        # Resolve absolute paths
        base = os.path.abspath(working_directory)
        target = os.path.abspath(os.path.join(working_directory, file_path))

        # Guardrail: ensure file is inside working directory
        if not target.startswith(base):
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

        # Check if file exists and is a regular file
        if not os.path.isfile(target):
            return f'Error: File not found or is not a regular file: "{file_path}"'

        # Read the file with truncation
        with open(target, "r", encoding="utf-8", errors="replace") as f:
            content = f.read(MAX_CHARS)

            # If content is truncated
            if len(content) == MAX_CHARS:
                content += f'\n[...File "{file_path}" truncated at {MAX_CHARS} characters]'

        return content

    except Exception as e:
        return f"Error: {str(e)}"
