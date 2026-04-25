import os

def write_file(working_directory, file_path, content):
    try:
        absolute_path = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(absolute_path, file_path))
        path_valid = os.path.commonpath([target_dir, absolute_path]) == absolute_path
        if not path_valid:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        if os.path.isdir(target_dir):
            return f'Error: Cannot write to "{file_path}" as it is a directory'
        parent_dir = os.path.dirname(target_dir)
        os.makedirs(parent_dir, exist_ok=True)
        with open(target_dir, "w") as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f"Error: {repr(e)}" 
