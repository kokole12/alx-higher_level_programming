#!/usr/bin/python3
""" a class for student"""


class Student:
    """ initializing the attributes for class student"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ returns the json representstion of the object"""
        return self.__dict__
