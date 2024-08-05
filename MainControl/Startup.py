import os

from Data.SystemPaths import SystemPaths
from MainControl.LoadChampionsAndSkins import load_champs
from MainControl.Saving import loading, saving
from MainControl.SearchForDependencyPrograms import search_for_league, search_for_ritobin


#es sollte also normalerweise ablaufen:
#lade gespeicherte daten
#suche pfade zu programmen wenn daten nicht gegeben, überprüfe gespeicherte Daten sonst
#lade champions
#lade anzahl der skins pro champion
#Zeige gui
def startup(root):
    champion_list, system_paths = loading()

    if system_paths is None:
        system_paths = SystemPaths(search_for_league(), search_for_ritobin(), "")
    if champion_list is None:
        champion_list = load_champs(system_paths)

    # check if paths exist
    if not os.path.isfile(system_paths.league_path):
        system_paths = SystemPaths(search_for_league(), system_paths.ritobin_path, system_paths.root_path)
    if not os.path.isfile(system_paths.ritobin_path):
        system_paths = SystemPaths(system_paths.league_path, search_for_ritobin(), system_paths.root_path)
    #todo check if root folder exist, or is none
    print(system_paths.league_path)
    print(system_paths.ritobin_path)

    #TODO Skins load skins from latest patch, look if new champ exist

    root.champion_list = champion_list
    root.system_paths = system_paths

    saving(champion_list, system_paths)
