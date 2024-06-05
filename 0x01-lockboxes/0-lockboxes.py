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
    seen_boxes = set([0])  # Set to keep track of visited (unlocked) boxes
    unseen_boxes = set(boxes[0]).difference(set([0]))  # Set of keys to be processed

    while unseen_boxes:
        boxIdx = unseen_boxes.pop()
        if boxIdx < 0 or boxIdx >= n:  # Ignore invalid box indices
            continue
        if boxIdx not in seen_boxes:
            unseen_boxes = unseen_boxes.union(boxes[boxIdx])  # Add new keys to be processed
            seen_boxes.add(boxIdx)  # Mark this box as seen

    return len(seen_boxes) == n  # Return True if all boxes have been seen
