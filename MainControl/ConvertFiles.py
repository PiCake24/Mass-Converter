import os
import subprocess


def ritobin(ritobin_path, root_path, champion, skin_number, direction):
    try:
        if direction:
            # Prepare the command list, direction bin to py
            command_list = [
                ritobin_path,
                os.path.join(root_path , 'data', 'characters', champion, 'skins', f'skin{skin_number}.bin'),
                os.path.join(root_path, 'data', 'characters', champion, 'skins', f'skin{skin_number}.py')
            ]
        else:
            # Prepare the command list, direction py to bin
            command_list = [
                ritobin_path,
                os.path.join(root_path, 'data', 'characters', champion, 'skins', f'skin{skin_number}.py'),
                os.path.join(root_path, 'data', 'characters', champion, 'skins', f'skin{skin_number}.bin')
            ]

        # Start the process
        subprocess.run(command_list, check=True)

        # Update the log
        print(f"{champion} {skin_number} .py created")

    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")
