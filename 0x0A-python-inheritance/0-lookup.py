#!/usr/bin/python3
"""lookup method"""


def lookup(obj):
    """retrun list of attributes and methods of `obj`

    Args:
        obj (object): object

    Returns:
        list: list of attributes
    """
    return dir(obj)
