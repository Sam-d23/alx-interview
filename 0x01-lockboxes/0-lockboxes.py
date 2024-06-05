#!/usr/bin/python3

def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened.
    
    Parameters:
    boxes (list of lists): A list where each element is a
    list of keys contained in the corresponding box.

    Returns:
    bool: True if all boxes can be opened, False otherwise.
    """
    n = len(boxes)
    seen_boxes = set([0])
    unseen_boxes = set(boxes[0]).difference(set([0]))

    while unseen_boxes:
        box_idx = unseen_boxes.pop()
        if box_idx < 0 or box_idx >= n:
            continue
        if box_idx not in seen_boxes:
            unseen_boxes = unseen_boxes.union(boxes[box_idx])
            seen_boxes.add(box_idx)

    return len(seen_boxes) == n
