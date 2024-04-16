#!/usr/bin/python3
""" write a string to a text file """


def write_file(filename="", text=""):
    """ write_file Writes a string to a text file (UTF8)
    and returns the number of characters written """
    with open(filename, 'w', encoding='utf-8') as f:
        return (f.write(text))
