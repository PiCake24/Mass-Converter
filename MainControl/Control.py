import time
import MainControl.ImportCdtb as icdtb
import MainControl.ConvertFiles as cv
import MainControl.WriteIntoFile as wif


def control(log_callback,stop_event, champions, path_variables):
    for i in range(1, 11):
        if stop_event.is_set():
            log_callback("Controlled task interrupted.")
            return
        log_callback(f"Task {i} in progress...")
        time.sleep(1)
    log_callback("Controlled task completed.")
    # get hashes
    log_callback("Getting hashes")
    icdtb.download_hashes()
    if stop_event.is_set():
        log_callback("Controlled task interrupted.")
    for champion in champions:
        filepath = path_variables.league_path + "\\DATA\\FINAL\\Champions\\" + champion + ".wad.client"
        outputpath = path_variables.root_Path + "\\0WADS"
        icdtb.unpack_file(filepath, outputpath)
        #for skin_number in champion.skin_list:
            #cv.ritobin(path_variables.ritobin_path, path_variables.root_path, champion, skin_number.skin_number)
            #wif.write_into(path_variables.root_path, champion, skin_number.skin_number, skin_number.size)
            #cv.ritobin(path_variables.ritobin_path, path_variables.root_path, champion, skin_number.skin_number)

    #unpack files
    #convert files
    #write into files
    #convert files back