#!/usr/bin/python3
""" a class for student"""


class Student:
    """ initializing the attributes for class student"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ returns the json representstion of the object"""
        if (type(attrs) == list and all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """ replaace all student attribes"""
        for k, v in json.items():
            setattr(self, k, v)
