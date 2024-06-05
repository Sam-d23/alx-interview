#!/usr/bin/python3

def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened.

    Parameters:
    boxes (list of lists): A list where each element is a list of keys contained in the corresponding box.

    Returns:
    bool: True if all boxes can be opened, False otherwise.
    """
    n = len(boxes)  # Number of boxes
    visited = set()  # Set to keep track of visited (unlocked) boxes
    stack = [0]  # Stack to manage the boxes to be processed, starting with the first box (index 0)

    # While there are boxes to be processed
    while stack:
        current_box = stack.pop()  # Take the last box from the stack
        if current_box not in visited:
            visited.add(current_box)  # Mark it as visited
            for key in boxes[current_box]:  # For each key in the current box
                if key < n:  # If the key corresponds to a valid box index, add it to the stack
                    stack.append(key)

    # Check if the number of visited boxes is equal to the total number of boxes
    return len(visited) == n
