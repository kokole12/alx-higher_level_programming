#!/usr/bin/python
""" module to  save object as JSON file"""
import json


def save_to_json_file(my_obj, filename):
    """ writes an object to a text file using JSON formatting"""
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
