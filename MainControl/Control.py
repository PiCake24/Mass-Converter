import time


def control(log_callback, stop_event):
    for i in range(1, 11):
        if stop_event.is_set():
            log_callback("Controlled task interrupted.")
            return
        log_callback(f"Task {i} in progress...")
        time.sleep(100)
    log_callback("Controlled task completed.")