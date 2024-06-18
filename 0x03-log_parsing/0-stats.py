#!/usr/bin/python3
"""
Script for parsing logs for HTTP requests.
"""
import re
import sys


def extract_input(line):
    """
    Extracts sections of an HTTP log line.
    """
    pattern = (
        r'\s*(?P<ip>\S+)\s* - \['
        r'(?P<date>[^\]]+)\] "GET /projects/260 HTTP/1.1" '
        r'(?P<status_code>\d{3}) (?P<file_size>\d+)\s*'
    )
    match = re.match(pattern, line)
    if match:
        return match.group('status_code'), int(match.group('file_size'))
    return None, 0

def print_statistics(total_size, status_counts):
    """
    Prints the accumulated statistics of the HTTP request log.
    """
    print(f"File size: {total_size}")
    for code, count in sorted(status_counts.items()):
        if count:
            print(f"{code}: {count}")

def update_metrics(line, total_size, status_counts):
    """
    Updates the metrics from a given HTTP request log line.
    """
    code, size = extract_input(line)
    if code:
        status_counts[code] += 1
        total_size += size
    return total_size

def main():
    """
    Starts the log parser.
    """
    total_size = 0
    line_count = 0
    status_counts = {str(code): 0 for code in [200, 301, 400, 401, 403, 404, 405, 500]}

    try:
        for line in sys.stdin:
            total_size = update_metrics(line.strip(), total_size, status_counts)
            line_count += 1
            if line_count % 10 == 0:
                print_statistics(total_size, status_counts)
    except (KeyboardInterrupt, EOFError):
        print_statistics(total_size, status_counts)
        raise
    finally:
        print_statistics(total_size, status_counts)


if __name__ == "__main__":
    run()

