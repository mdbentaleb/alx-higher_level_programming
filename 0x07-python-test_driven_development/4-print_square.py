#!/usr/bin/python3
""" square-printing function """


def print_square(size):
    """ print a squarewith the # character

    Args:
        size: the height/width ofthesquare
    Raises:
        TypeError: if sizeisnot an integer
        ValueError: if size is < 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for a in range(size):
        [print("#", end="") for p in range(size)]
        print("")
