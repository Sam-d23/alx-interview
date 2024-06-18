#!/usr/bin/python3


import sys
import signal
import re


total_file_size = 0
status_code_counts = {"200": 0, "301": 0, "400": 0, "401": 0,
                      "403": 0, "404": 0, "405": 0, "500": 0}
line_count = 0

log_pattern = re.compile(r'^\S+ - \[\S+ \S+\] "GET /projects/260 HTTP/1.1" (\d{3}) (\d+)$')

def print_stats():
    """Prints stats"""
    print(f"File size: {total_file_size}")
    for code in sorted(status_code_counts):
        if status_code_counts[code] > 0:
            print(f"{code}: {status_code_counts[code]}")

def handle_interrupt(sig, frame):
    """Handles interrupt"""
    print_stats()
    sys.exit(0)

signal.signal(signal.SIGINT, handle_interrupt)

try:
    for line in sys.stdin:
        line = line.strip()
        match = log_pattern.match(line)
        if match:
            status_code, file_size = match.groups()
            total_file_size += int(file_size)
            status_code_counts[status_code] += 1
            line_count += 1
            if line_count % 10 == 0:
                print_stats()

except KeyboardInterrupt:
    handle_interrupt(signal.SIGINT, None)

finally:
    print_stats()

