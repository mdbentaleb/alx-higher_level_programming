#!/usr/bin/python3
""" class student"""


class Student:
    """newclass student"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return (self.__dict__)
        else:
            dic = {}
            for n in attrs:
                if hasattr(self, n):
                    dic[n] = getattr(self, n)
            return (dic)
