import os
import re

from cdtb.hashes import default_hash_dir

from Data.Champion import Champion
from Data.Skin import Skin
from MainControl.ImportCdtb import download_hashes


def load_champs(liste, path_variables):
    folder_path = path_variables.league_path[:len(path_variables.league_path) - 22] + "\\DATA\\FINAL\\Champions\\"
    try:
        # List all files and directories in the specified folder
        items = os.listdir(folder_path)

        # Filter out directories, keeping only files
        files = [item for item in items if os.path.isfile(os.path.join(folder_path, item))]

        files = [file.split('.')[0].lower() for file in files]
        # get rid of duplicates
        files = list(set(files))

    except Exception as e:
        return str(e)

    #download hashes
    download_hashes()

    # get path to hashes:
    path = default_hash_dir
    substrings = ["tft", "pet", "cherry", "doom", "nexusblitz", "odyssey", "sg", "sru", "ap_viking",
                  "jammerdevice", "ightmarebots_malzahar_riftherald", "npc_k", "npc_s", "npc_v", "test",
                  "tutorial", "ultbook"]
    # open game hash
    with open(os.path.join(path, "hashes.game.txt"), "r") as file:
        r = False
        for line in file:
            line = line[17:]
            if not line.startswith("data/characters") and r is False:
                pass
            elif line.startswith("data/characters"):
                r = True
                line = line[16:]
                first_part = line.split('/', 1)[0]
                if (any(file in first_part for file in files) and
                        not any(sub in first_part for sub in substrings) and
                        all(champion.champion != first_part for champion in liste)):
                    champ = Champion(first_part, [])
                    liste.append(champ)
                for champion in liste:
                    if champion.champion == first_part:
                        load_skins(line, champion)
            else:
                for champion in liste:
                    champion.skin_list.sort(key=lambda skin: skin.skin_number)
                print(len(liste))
                return liste


def load_skins(line, champion):
    line = line.split('/', 1)[1]
    pattern = r'^skins/skin\d+\.bin$'
    if re.match(pattern, line):
        print(line)
        line = line[10:-5]
        if all(skin.skin_number != line for skin in champion.skin_list):
            skin = Skin(int(line), 1)
            champion.skin_list.append(skin)
