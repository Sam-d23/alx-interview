#!/usr/bin/env python3
"""
Script to compute metrics from log data input via stdin.

Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
"""

import sys
import re
import signal


# Dictionary to store counts of status codes
status_code_counts = {
    200: 0,
    301: 0,
    400: 0,
    401: 0,
    403: 0,
    404: 0,
    405: 0,
    500: 0
}

total_file_size = 0
line_count = 0

def print_statistics(signal, frame):
    """
    Print statistics for total file size and number of lines by status code.
    """
    print(f"Total file size: {total_file_size} bytes")
    for code in sorted(status_code_counts.keys()):
        if status_code_counts[code] > 0:
            print(f"{code}: {status_code_counts[code]}")
    sys.exit(0)

# Register the signal handler for SIGINT (Ctrl+C)
signal.signal(signal.SIGINT, print_statistics)

# Regex pattern to match the log entry format
log_pattern = r'^(\d+\.\d+\.\d+\.\d+) - \[.*\] "GET /projects/260 HTTP/1\.1" (\d+) (\d+)$'

try:
    for line in sys.stdin:
        line = line.strip()
        
        # Match the log entry format
        match = re.match(log_pattern, line)
        if not match:
            continue
        
        # Extract components from the matched pattern
        status_code = int(match.group(2))
        file_size = int(match.group(3))
        
        # Update total file size
        total_file_size += file_size
        
        # Update status code counts
        if status_code in status_code_counts:
            status_code_counts[status_code] += 1
        
        # Increment line count
        line_count += 1
        
        # Print statistics every 10 lines
        if line_count % 10 == 0:
            print_statistics(None, None)


except KeyboardInterrupt:
    # Handle keyboard interruption (Ctrl+C)
    print_statistics(None, None)

