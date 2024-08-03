#check if a necessary variables are set

def check_inputs(log_callback, path_variables):
    if path_variables.riot_path is None:
        log_callback("No Riot Path set")
        return False
    if path_variables.ritobin_path is None:
        log_callback("No Ritobin Path set")
        return False
    if path_variables.root_path is None:
        log_callback("No Root Path set")
        return False
    return True
