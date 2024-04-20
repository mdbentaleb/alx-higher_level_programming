#!/usr/bin/python3
""" module for Base class """
from json import dumps, loads
import csv


class Base:
    """A representation of the foundation of our (OOP) hierarchy """

    __nb_objects = 0

    def __init__(self, id=None):
        """ constructor """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
