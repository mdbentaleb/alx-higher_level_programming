#!/usr/bin/python3
""" Append a string to a file """


def append_write(filename="", text=""):
    """ Appends a string and returns the number
    of characters added """
    with open(filename, 'a', encoding="utf-8") as f:
        return (f.write(text))
