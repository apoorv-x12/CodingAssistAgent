# pylint: disable=broad-exception-caught
# tools/replace_in_file.py

import os

def replace_in_file(working_directory, file_path, old_text, new_text):
    """
    Replace the first occurrence of old_text with new_text in the specified file.
    This is much more efficient than rewriting entire files for small edits.
    """
    try:
        base = os.path.abspath(working_directory)
        target = os.path.abspath(os.path.join(working_directory, file_path))
        
        # Guardrail: ensure the target is inside working_directory
        if not target.startswith(base):
            return f'Error: Cannot access "{file_path}" as it is outside the permitted working directory'
        
        # Check if file exists
        if not os.path.isfile(target):
            return f'Error: File not found: "{file_path}"'
        
        # Read the file
        with open(target, "r", encoding="utf-8", errors="replace") as f:
            content = f.read()
        
        # Check if old_text exists in the file
        if old_text not in content:
            return f'Error: The specified text was not found in "{file_path}". Make sure old_text matches exactly.'
        
        # Replace the first occurrence
        new_content = content.replace(old_text, new_text, 1)
        
        # Write back to file
        with open(target, "w", encoding="utf-8", errors="replace") as f:
            f.write(new_content)
        
        return f'Successfully replaced text in "{file_path}"'
        
    except Exception as e:
        return f"Error: {str(e)}"
