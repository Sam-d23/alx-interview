#!/usr/bin/python3
"""
log parsing.
"""


import sys
import re
import signal
from collections import defaultdict


status_code_counts = defaultdict(int)
total_file_size = 0
line_count = 0


def print_statistics(signal, frame):
    """
    Prints the accumulated statistics.
    """
    print(f"File size: {total_file_size}")
    for code in sorted(status_code_counts.keys()):
        if status_code_counts[code] > 0:
            print(f"{code}: {status_code_counts[code]}")
    sys.exit(0)


# Register the signal handler for SIGINT (Ctrl+C)
signal.signal(signal.SIGINT, print_statistics)

# Regex pattern to match the log entry format
log_pattern = (
    r'^(\d+\.\d+\.\d+\.\d+) - \[.*\] "GET /projects/260 HTTP/1\.1" '
    r'(\d+) (\d+)$'
)

try:
    for line in sys.stdin:
        line = line.strip()

        # Match the log entry format
        match = re.match(log_pattern, line)
        if not match:
            continue

        try:
            status_code = int(match.group(2))
            file_size = int(match.group(3))

            # Update total file size
            total_file_size += file_size

            # Update status code counts
            if status_code in {200, 301, 400, 401, 403, 404, 405, 500}:
                status_code_counts[status_code] += 1

            # Increment line count
            line_count += 1

            # Print statistics every 10 lines
            if line_count % 10 == 0:
                print_statistics(None, None)

        except ValueError:
            continue

except KeyboardInterrupt:
    print_statistics(None, None)

