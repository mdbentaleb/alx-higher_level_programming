#!/usr/bin/python3
""" class square """


class Square:
    """ square """

    def __init__(self, size=0):
        """ initialize a square

        Args:
            size (int): size of new square
        """
        self.size = size

    @property
    def size(self):
        """ get current size of square """
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ return area of square """
        return (self.__size * self.__size)

    def __eq__(self, other):
        """ comparision to a square """
        return self.area() == other.area()

    def __ne__(self, other):
        """ comparison to a square """
        return self.area() != other.area()

    def __lt__(self, other):
        """ comparison to a square """
        return self.area() < other.area()

    def __le__(self, other):
        """ comparison to a square """
        return self.area() <= other.area()

    def __gt__(self, other):
        """ comparison to a square """
        return self.area() > other.area()

    def __ge__(self, other):
        """ compmarison to a square """
        return self.area() >= other.area()
