import os


def search_for_ritobin():
    drives = [f"{d}:\\" for d in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' if os.path.exists(f"{d}:\\")]
    for root_dir in drives:
        for root, dirs, files in os.walk(root_dir):
            # Check if 'Riot Games' is in the current directory
            if 'ritobin_gui.exe' in files:
                return os.path.join(root, "ritobin_gui.exe")
    return None

def search_for_league():
    drives = [f"{d}:\\" for d in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' if os.path.exists(f"{d}:\\")]
    for root_dir in drives:
        for root, dirs, files in os.walk(root_dir):
            # Check if 'Riot Games' is in the current directory
            if 'Riot Games' in dirs:
                riot_games_path = os.path.join(root, 'Riot Games')

                # Check if 'League of Legends' is in 'Riot Games' directory
                if 'League of Legends' in os.listdir(riot_games_path):
                    lol_path = os.path.join(riot_games_path, 'League of Legends')

                    # Check if 'Game' is in 'League of Legends' directory
                    if 'Game' in os.listdir(lol_path):
                        game_path = os.path.join(lol_path, 'Game')
                        print(f"Found 'Game' folder at: {game_path}")
                        return game_path
    return None


#print(search_for_league())
print(search_for_ritobin())