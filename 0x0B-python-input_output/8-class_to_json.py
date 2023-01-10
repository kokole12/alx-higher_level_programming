#!/usr/bin/python3
""" module for a class to json format"""


def class_to_json(obj):
    """ returns a dictionary from the object file passed"""
    return obj.__dict__
