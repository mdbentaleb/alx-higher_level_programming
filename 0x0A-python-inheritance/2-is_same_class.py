#!/usr/bin/python3
"""checks if an object is an instance of a specified class"""


def is_same_class(obj, a_class):
    """return True if obj is instance of a_class"""
    j = type(obj)
    if j == a_class:
        return True
    return False
