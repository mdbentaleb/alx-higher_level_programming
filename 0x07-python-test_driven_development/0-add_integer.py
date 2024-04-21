#!/usr/bin/python3
""" integer addition function """


def add_integer(a, b=98):
    """ return int addition of a and b

    Float arguments are typecasted to ints before addition is performed.

    Raises:
        TypeError: if a, b are not int, float.
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
