import os
from config import MAX_CHAR

def get_file_content(working_directory, file_path):
    try:
        absolute_path = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(absolute_path, file_path))
        path_valid = os.path.commonpath([target_dir, absolute_path]) == absolute_path
        if not path_valid:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(target_dir):
            return f'Error: File not found or is not a regular file: "{file_path}"'
        file_content = ''
        with open(target_dir, "r") as f:
            file_content = f.read(MAX_CHAR)
            # checking if file was truncated by checking if 10001 char exists
            if f.read(1):
                file_content += f'[...File "{file_path}" truncated at {MAX_CHAR} characters]'
        return file_content
    except Exception as e:
        return f"Error: {repr(e)}"