#!/usr/bin/python3
""" this module defines a Josn to object formula"""
import json


def from_json_string(my_str):
    """ returns the object represented by json"""
    return json.loads(my_str)
