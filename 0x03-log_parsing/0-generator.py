#!/usr/bin/python3
import random
import sys
import datetime
from time import sleep

for _ in range(10000):
    ip_address = ".".join(str(random.randint(1, 255)) for _ in range(4))
    status_code = random.choice([200, 301, 400, 401, 403, 404, 405, 500])
    file_size = random.randint(1, 1024)
    current_time = datetime.datetime.now().strftime("%d/%b/%Y:%H:%M:%S %z")
    
    log_entry = f"{ip_address} - [{current_time}] \"GET /projects/260 HTTP/1.1\" {status_code} {file_size}\n"
    
    sys.stdout.write(log_entry)
    sys.stdout.flush()
    sleep(random.random())
