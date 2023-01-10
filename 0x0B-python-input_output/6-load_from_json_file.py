#!/usr/bin/python3
""" module that loads an object from json file"""
import json


def load_from_json_file(filename):
    """ loading the object from a json file"""
    with open(filename) as f:
        json.load(f)
