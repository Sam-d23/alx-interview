#!/usr/bin/python3
'''Checks whether all the boxes can be opened
'''


def canUnlockAll(boxes):
    '''
    Prototype: def canUnlockAll(boxes)\
    boxes is a list of lists
    A key labelled the same number as a box\
            opens that box\
    all keys are taken to be positive integers\
        There can be keys that do not have boxes\
    The first box boxes[0] is unlocked\
    Return True if all boxes can be opened, else return False\

    '''
    n = len(boxes)
    checked_boxes = set([0])
    unchecked_boxes = set(boxes[0]).difference(set([0]))
    while len(unchecked_boxes) > 0:
        boxIdx = unchecked_boxes.pop()
        if not boxIdx or boxIdx >= n or boxIdx < 0:
            continue
        if boxIdx not in seen_boxes:
            unchecked_boxes = unchecked_boxes.union(boxes[boxIdx])
            checked_boxes.add(boxIdx)
    return n == len(checked_boxes)
