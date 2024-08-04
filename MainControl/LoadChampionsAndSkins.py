import os

from Data.Champion import Champion
from Data.SystemPaths import System_paths
from MainControl.SearchForDependencyPrograms import search_for_league


def load_champs(path_variables):
    folder_path = path_variables.riot_path + "\\DATA\\FINAL\\Champions\\"
    try:
        # List all files and directories in the specified folder
        items = os.listdir(folder_path)

        # Filter out directories, keeping only files
        files = [item for item in items if os.path.isfile(os.path.join(folder_path, item))]

        files = [file.split('.')[0] for file in files]

        files = list(set(files))

        files.sort()

        champions = []

        for champion in files:
            champ = Champion(champion, [], False)
            champions.append(champ)

        return champions
    except Exception as e:
        return str(e)

def loadskins():
    pass
    #unpacke champion nach champion und schaue nach welche skins sie haben
    #wir brauchen vorher hashes

#wir müssen auch noch den patch mit dem aktuellen patch vergleichen und wenn wir einen patch haben laden wir nur die neusten skins neu (das sollte viel schneller gehen)
#+speichern und laden
#auch sollte ich mir gedanken darüber machen, was passiert wenn das programm league nicht findet.(root und ritobin sind ja hierfür egal)

#es sollte also normalerweise ablaufen:
#lade gespeicherte daten
#suche pfade zu programmen wenn daten nicht gegeben, überprüfe gespeicherte Daten sonst
#lade champions
#lade anzahl der skins pro champion
#Zeige gui

#reduizierung der größe der championliste
#change color palette
if __name__ == "__main__":
    folder_path = search_for_league()
    print(folder_path)
    paths = System_paths(folder_path,"","")
    files = load_champs(paths)
    print(files)