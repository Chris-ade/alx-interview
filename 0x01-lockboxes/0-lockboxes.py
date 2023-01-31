#!/usr/bin/python3
"""
Returns a boolean which determines if all the boxes can be opened.
"""


def canUnlockAll(boxes):
    opened_boxes = set()
    opened_boxes.add(0)
    
    stack = [0]
    while stack:
        box = stack.pop()
        for key in boxes[box]:
            if key not in opened_boxes:
                opened_boxes.add(key)
                stack.append(key)
    
    return len(opened_boxes) == len(boxes)
