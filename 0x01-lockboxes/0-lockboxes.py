#!/usr/bin/python3
""" Defines lockboxes """


def canUnlockAll(boxes):
    """ Determines whether all boxes can be unlocked or not
    Returns: True if all boxes can be unlocked  and
             False if not
             """
    keys = [0]
    for key in keys:
        for val in boxes[key]:
            if val not in keys:
                keys.append(val)
    if len(keys) == len(boxes):
        return True
    return False
