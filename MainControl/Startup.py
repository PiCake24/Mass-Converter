from Data.SystemPaths import System_paths
from MainControl.LoadChampionsAndSkins import load_champs
from MainControl.Saving import loading
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
        system_paths = System_paths(search_for_league(), search_for_ritobin(), "")
    if champion_list is None:
        champion_list = load_champs(system_paths)
    root.champion_list = champion_list
    root.system_paths = system_paths
