#!/usr/bin/python3
"""def class_to_json"""


def class_to_json(obj):
    """ Serializes class instance. """
    return obj.__dict__
