#!/usr/bin/python3
import random
import sys
from time import sleep
import datetime

# Generate and write 10000 log entries
for _ in range(10000):
    # Sleep for a random time interval
    sleep(random.random())
    
    # Generate random components for the log entry
    ip_address = ".".join(str(random.randint(1, 255)) for _ in range(4))
    date_time = datetime.datetime.now()
    status_code = random.choice([200, 301, 400, 401, 403, 404, 405, 500])
    file_size = random.randint(1, 1024)
    
    # Construct and write the log entry
    sys.stdout.write(f"{ip_address} - [{date_time}] \"GET /projects/260 HTTP/1.1\" {status_code} {file_size}\n")
    sys.stdout.flush()
