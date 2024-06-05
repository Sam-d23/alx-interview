#!/usr/bin/python3
"""Solves the lock boxes puzzle."""


def canUnlockAll(boxes):
    """
    Check if all boxes can be opened.

    Args:
        boxes (list): List which contain all the boxes with the keys.

    Returns:
        bool: True if all boxes can be opened, otherwise, False.
    """
    n = len(boxes)
    seen = set()
    stack = [0]

    while stack:
        current_box = stack.pop()
        if current_box not in seen:
            seen.add(current_box)
            stack.extend(boxes[current_box])

    return len(seen) == n


def main():
    """Entry point."""
    canUnlockAll([[]])


if __name__ == '__main__':
    main()

