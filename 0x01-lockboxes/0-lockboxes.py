#!/usr/bin/python3

def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened.
    
    Parameters:
    boxes (list of lists): A list where each element is a list of keys contained in the corresponding box.

    Returns:
    bool: True if all boxes can be opened, False otherwise.
    """
    # Number of boxes
    n = len(boxes)
    
    # Set to keep track of visited (unlocked) boxes
    visited = set()
    
    # Stack to manage the boxes to be processed, starting with the first box (index 0)
    stack = [0]
    
    # While there are boxes to be processed
    while stack:
        # Take the last box from the stack
        current_box = stack.pop()
        
        # If the box has not been visited (unlocked) yet
        if current_box not in visited:
            # Mark it as visited
            visited.add(current_box)
            
            # For each key in the current box
            for key in boxes[current_box]:
                # If the key corresponds to a valid box index, add it to the stack
                if key < n:
                    stack.append(key)
    
    # Check if the number of visited boxes is equal to the total number of boxes
    # If true, all boxes can be unlocked
    return len(visited) == n

