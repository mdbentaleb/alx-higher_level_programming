#!/usr/bin/python3
""" student class """


class Student:
    """new student class"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary"""
        if attrs is None:
            return (self.__dict__)
        else:
            dic = {}
            for n in attrs:
                if hasattr(self, n):
                    dic[n] = getattr(self, n)
            return (dic)

    def reload_from_json(self, json):
        """Replaces all attributes"""
        save = vars(self)
        for ky, value in json.items():
            save[ky] = value
