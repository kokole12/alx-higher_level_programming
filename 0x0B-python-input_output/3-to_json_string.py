#!/usr/bin/python3
""" module that defines a string to the json function"""
import json


def to_json_string(my_obj):
    """ returns a json represntation of my_obj"""
    return json.dumps(my_obj)
