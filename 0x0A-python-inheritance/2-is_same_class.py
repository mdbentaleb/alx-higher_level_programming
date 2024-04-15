#!/usr/bin/python3
"""is_same_class method module"""


def is_same_class(obj, a_class):
    """determines if an object is exactly an instance of a class"""
    return type(obj) == a_class
