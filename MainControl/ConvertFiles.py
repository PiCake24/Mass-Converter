import os
import subprocess

def ritobin(ritobin_path, root_path, champion, skin_number):
    try:
        # Prepare the command list
        command_list = [
            ritobin_path,
            os.path.join(root_path , 'data', 'characters', champion, 'skins', f'skin{skin_number}.bin'), #TODO give ending as proper parameter, or just define direction
            os.path.join(root_path, 'data', 'characters', champion, 'skins', f'skin{skin_number}.py')
        ]

        # Start the process
        subprocess.run(command_list, check=True)

        # Update the log
        print(f"{champion} {skin_number} .py created")

    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")