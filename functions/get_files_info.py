import os

def get_files_info(working_directory, directory="."):
    working_directory_abs_path = os.path.abspath(working_directory)
    target_dir = os.path.normpath(os.path.join(working_directory_abs_path, directory))
    try:
        path_valid = os.path.commonpath([target_dir, working_directory_abs_path]) == working_directory_abs_path
    except Exception as e:
        return f"Error: {repr(e)}"
    if not path_valid:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not os.path.isdir(target_dir):
        return f'Error: "{directory}" is not a directory'
    output = []
    contents = os.listdir(target_dir)
    for content in contents:
        try:
            file_path = os.path.join(target_dir, content)
            file_size = os.path.getsize(file_path)
            is_dir = os.path.isdir(file_path)
            output_str = f"- {content}: file_size={file_size} bytes, is_dir={is_dir}"
            output.append(output_str)
        except Exception as e:
            return f"Error: {repr(e)}"
    return '\n'.join(output)