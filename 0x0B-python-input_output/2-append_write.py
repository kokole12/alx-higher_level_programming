#!/usr/bin/python3
""" module that appends to a given files"""


def append_write(filename="", text=""):
    """ appending some given text to a files"""
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
