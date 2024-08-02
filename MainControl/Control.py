import time


def control(log_callback, champions, path_variables):
    for i in range(1, 11):
        log_callback(f"Task {i} in progress...")
        time.sleep(100)
    log_callback("Controlled task completed.")
    #get hashes
    #unpack files
    #convert files
    #write into files
    #convert files back