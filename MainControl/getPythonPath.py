import subprocess

def get_python_path_windows():
    try:
        # Run `where python` command to find Python executable path
        process = subprocess.Popen(["cmd.exe", "/c", "where", "python"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        stdout, stderr = process.communicate()

        # Decode the output to string and split lines
        output = stdout.decode("utf-8").strip()
        lines = output.splitlines()

        # Take the first line if available
        if lines:
            python_path = lines[0].strip()

            # Remove 'python.exe' from the end of the path
            if python_path.lower().endswith("\\python.exe"):
                python_path = python_path[:-len("\\python.exe")]

            # Append '\Scripts' to the path
            scripts_path = python_path + "\\Scripts"

            # Ensure the path ends with '\\'
            if not scripts_path.endswith("\\"):
                scripts_path += "\\"

            # Print or log the path
            print("PythonPath:", scripts_path)

            return scripts_path

    except Exception as e:
        print(f"Error while getting Python path: {e}")

    return None

# Example usage:
if __name__ == "__main__":
    python_scripts_path = get_python_path_windows()
    if python_scripts_path:
        print("Python Scripts Path:", python_scripts_path)
    else:
        print("Python path not found.")
