import json

from Data.Champion import Champion
from Data.Skin import Skin
from Data.SystemPaths import System_paths

def champion_to_dict(champion):
    return {
        'champion': champion.champion,
        'skin_list': [vars(skin) for skin in champion.skin_list],
        'active': champion.active,
        'hidden': champion.hidden
    }

def system_paths_to_dict(system_paths):
    return vars(system_paths)
def saving(champion_list, system_paths):
    data = {
        'championList': [champion_to_dict(champ) for champ in champion_list],
        'system_paths': system_paths_to_dict(system_paths)
    }
    with open('data.json', 'w') as file:
        json.dump(data, file, indent=4)

def dict_to_skin(d):
    return Skin(d['skin_number'], d['size'], d['active'])

def dict_to_champion(d):
    skin_list = [dict_to_skin(s) for s in d['skin_list']]
    champ = Champion(d['champion'], skin_list, d['active'])
    champ.hidden = d['hidden']
    return champ

def dict_to_system_paths(d):
    return System_paths(d['riot_path'], d['ritobin_path'], d['root_path'])
def loading():
    try:
        with open('data.json', 'r') as file:
            data = json.load(file)

        championList = [dict_to_champion(champ_dict) for champ_dict in data['championList']]
        system_paths = dict_to_system_paths(data['system_paths'])
        return championList, system_paths

    except FileNotFoundError or json.JSONDecodeError:
        return None, None
