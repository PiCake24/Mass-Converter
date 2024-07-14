import time


def control(log_callback):
    for i in range(1, 11):
        log_callback(f"Task {i} in progress...")
        time.sleep(100)
    log_callback("Controlled task completed.")