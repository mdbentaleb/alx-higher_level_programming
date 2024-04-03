#!/usr/bin/python3
""" class magicClass"""
import math


class MagicClass:
    """ magicClass """
    def __init__(self, radius=0):
        """ initializes """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """ set area """
        return (self.__radius ** 2) * math.pi

    def circumference(self):
        """ get circumference """
        return (2 * math.pi * self.__radius)
