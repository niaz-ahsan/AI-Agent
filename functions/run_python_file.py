import os
import subprocess
from google.genai import types

def run_python_file(working_directory, file_path, args=None):
    try:    
        absolute_path = os.path.abspath(working_directory)
        full_file_path = os.path.normpath(os.path.join(absolute_path, file_path))
        path_valid = os.path.commonpath([full_file_path, absolute_path]) == absolute_path
        if not path_valid:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(full_file_path):
            return f'Error: "{file_path}" does not exist or is not a regular file'
        _ , file_extension = os.path.splitext(full_file_path)
        if file_extension != '.py':
            return f'Error: "{file_path}" is not a Python file'
        command = ["python3", full_file_path]
        if args is not None:
            command.extend(args)
        command_output = subprocess.run(
            command,
            cwd=absolute_path,
            capture_output=True,
            text=True,
            timeout=30
        )
        output_str = []
        if len(command_output.stdout) < 1 and len(command_output.stderr) < 1:
            output_str.append("No output produced")
        else:
            if command_output.stdout:
                output_str.append(f"STDOUT: {command_output.stdout}")
            if command_output.stderr:
                output_str.append(f"STDERR: {command_output.stderr}")
        if command_output.returncode != 0:
            output_str.append(f"Process exited with code {command_output.returncode}")
        return "\n".join(output_str)
    except Exception as e:
        return f"Error: executing Python file: {e}"
    
schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="The function will execute a python script specified in the file path, relative to the working directory. Additional arguments can be provided.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path of the python script, relative to the working directory",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                description="Additional arguments that should be passed with the shell command",
                items=types.Schema(
                    type=types.Type.STRING,
                    description="considered to be an argument to the python script"
                )
            ),
        }
    ),
)
    