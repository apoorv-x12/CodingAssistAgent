# functions/get_files_info.py

import os

def get_files_info(working_directory, directory="."):
    try:
        # Resolve paths
        base = os.path.abspath(working_directory)
        target = os.path.abspath(os.path.join(working_directory, directory))

        # Guardrail: ensure the target is inside base
        if not target.startswith(base):
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

        # Must be a directory
        if not os.path.isdir(target):
            return f'Error: "{directory}" is not a directory'

        # Build listing
        entries = []
        for name in os.listdir(target):
            path = os.path.join(target, name)
            size = os.path.getsize(path)

            is_dir = os.path.isdir(path)
            entries.append(f"- {name}: file_size={size} bytes, is_dir={is_dir}")

        return "\n".join(entries)

    except Exception as e:
        return f"Error: {str(e)}"
