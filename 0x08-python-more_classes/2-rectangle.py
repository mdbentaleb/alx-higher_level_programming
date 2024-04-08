#!/usr/bin/python3
""" rectangle class """


class Rectangle:
    """ rectangle representation """

    def __init__(self, width=0, height=0):
        """ new Rectangle

        Args:
            width (int): new rectangle width
            height (int): new rectangle height
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ get the width of the rectangle """
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ get the height of the rectangle """
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ return rectangle area """
        return (self.__width * self.__height)

    def perimeter(self):
        """ the perimeter of the Rectangle """
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))
