#!/usr/bin/python3
""" this function add the attributes of an object"""


def add_attribute(obj, att, val):
    """ adds new attribute to object if possible"""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add attribute")
    setattr(obj, att, val)
