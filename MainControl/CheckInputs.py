#check if a necessary variables are set

def check_inputs(champions, path_variables):
    if len(champions) == 0:
        return False
    for champion in champions:
        if len(champion.skin_list) == 0:
            return False
    if path_variables.riot_path is None or path_variables.ritobin_path is None or path_variables.root_path is None:
        return False
    return True
