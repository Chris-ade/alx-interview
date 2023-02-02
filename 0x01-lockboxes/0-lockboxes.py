#!/usr/bin/python3
"""
Returns a boolean which determines if all the boxes can be opened.
"""


def canUnlockAll(boxes):
    """
    Returns a Boolean
    Parameters:
    boxes (list): A list of lists to be checked.
    Returns:
    True if all boxes can be opened, else return False.
    """
    if ((type(boxes) is not list) or len(boxes) == 0):
        return False
    for k in range(1, len(boxes) - 1):
        boxes_checked = False
        for idx in range(len(boxes)):
            boxes_checked = k in boxes[idx] and k != idx
            if boxes_checked:
                break
        if boxes_checked is False:
            return boxes_checked
    return True

