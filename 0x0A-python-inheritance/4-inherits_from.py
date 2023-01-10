#!/usr/bin/python3
""" checks if an object is an instance of a subclass"""


def inherits_from(obj, a_class):
    """ checks if an object is from a subclass of a given super class"""
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
