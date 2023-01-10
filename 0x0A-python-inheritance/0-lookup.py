#!/usr/bin/pyhton3
""" this module returns list of available
attributes and methods of an object"""


def lookup(obj):
    """ Returns all the methods and functions to the object"""

    return dir(obj)
