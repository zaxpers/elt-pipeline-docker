import datetime

with open("/app/log.txt","a") as log_file:
    log_file.write(f"Current time: {datetime.datetime.now()}\n")