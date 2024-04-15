#!/usr/bin/python3
"""
lookup - a function that returns the list of available attributes and methods of an object
"""


def lookup(obj):
    """retrun list of attributes and methods of "obj"

    Args:
        obj: object

    Returns:
        list of attributes and members
    """
    return dir(obj)
