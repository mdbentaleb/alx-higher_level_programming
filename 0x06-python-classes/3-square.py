#!/usr/bin/python3
"""class square """


class Square:
    """class square"""

    def __init__(self, size=0):
        """ constructor of a square """
        if (type(size) is not int):
            raise (TypeError("size must be an integer"))
        elif (size < 0):
            raise (ValueError("size must be >= 0"))
        else:
            self.__size = size

    def area(self):
        """ area of the square """
        return (self.__size ** 2)
