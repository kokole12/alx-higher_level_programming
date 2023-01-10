#!/usr/bin/python3
""" A class for Basic Geometry"""


class BaseGeometry:
    """ an empty class"""
    pass

    def area():
        """ method not implemented"""

        raise Exception("area() is not yet implemented")

    def integer_validator(self, name, value):
        """ validate that a value is an integer"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
