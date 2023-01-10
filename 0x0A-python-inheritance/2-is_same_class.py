#!/usr/bin/python3
""" checks if an objct is an instance of a
given class
"""


def is_same_class(obj, a_class):
    """ return true if the object is an instance of the class"""
    return (type(obj) == a_class)
