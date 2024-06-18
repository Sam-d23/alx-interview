#!/usr/bin/python3

"""
Log parsing project.
"""


import sys
import re
import signal
from collections import defaultdict


# Dictionary to store counts of status codes
status_code_counts = defaultdict(int)
total_file_size = 0
line_count = 0

def print_statistics(signal, frame):
    """
    Reads stdin line by line and computes metrics.
    """
    print(f"Total file size: {total_file_size} bytes")
    for code in sorted(status_code_counts.keys()):
        if status_code_counts[code] > 0:
            print(f"{code}: {status_code_counts[code]}")
    sys.exit(0)

signal.signal(signal.SIGINT, print_statistics)

log_pattern = r'^\d+\.\d+\.\d+\.\d+ - \[.*\] "GET /projects/260 HTTP/1\.1" (\d+) (\d+)$'

try:
    for line in sys.stdin:
        line = line.strip()
        
        match = re.match(log_pattern, line)
        if not match:
            continue
        
        try:
            status_code, file_size = map(int, match.groups())
            if status_code in {200, 301, 400, 401, 403, 404, 405, 500}:
                total_file_size += file_size
                status_code_counts[status_code] += 1
                line_count += 1
        
                if line_count % 10 == 0:
                    print_statistics(None, None)
        
        except ValueError:
            continue

except KeyboardInterrupt:
    print_statistics(None, None)

