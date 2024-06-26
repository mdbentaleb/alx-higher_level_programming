#!/usr/bin/python3
""" class Rectangle """


class Rectangle:
    """
        class Rectangle defines a rectangle
        Attributes:
            width (int): rectangle width
            height (int): rectangle height
    """
    def __init__(self, width=0, height=0):
        """
            initialises the instances
            Args:
                width (int): the rectangle width
                height (int): the rectangle height
        """
        if isinstance(width, int):
            if width < 0:
                raise ValueError("width must be >= 0")
            self.__width = width
        else:
            raise TypeError("width must be an integer")

        if isinstance(height, int):
            if height < 0:
                raise ValueError("height must be >= 0")
            self.__height = height
        else:
            raise TypeError("height must be an integer")

    @property
    def width(self):
        """
            getter function for private attribute width
            Retruns: width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
            setter function for private attribute width
            Args:
                value (int): new width value
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
            getter function for private attribute height
            Returns: height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
            setter function for the private attribute height
            Args:
                value (int): new height value
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
            public instance method to calculate area of rectangle
            Returns: area of rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """
            public instance method to calculate the perimeter of a rectangle
            Returns: perimeter of rectangle
        """
        if self.__width is 0 or self.__height is 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
            return string representation of a rectangle
        """
        rectangle = ""
        if self.__width is 0 or self.__height is 0:
            return rectangle

        for a in range(self.__height - 1):
            rectangle += "#" * self.__width + "\n"
        rectangle += "#" * self.__width

        return rectangle

    def __repr__(self):
        """
            returns the rectangle string representation
            representation able to be recreated into a new instance
            using eval
        """
        rectangle = ''
        if self.__width is 0 or self.__height is 0:
            return rectangle
        rectangle = 'Rectangle({}, {})'.format(self.__width, self.__height)
        return rectangle

    def __del__(self):
        """
            prints Bye rectangle... when an instance is
            deleted
        """
        print('Bye rectangle...')
