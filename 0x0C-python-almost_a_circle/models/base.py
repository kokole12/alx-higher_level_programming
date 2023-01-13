#!/usr/bin/python3
""" Initializing a class base"""


class Base:
    """ class variable to keep track of the instances of base"""

    __nd_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nd_objects += 1
            self.id = Base.__nd_objects
