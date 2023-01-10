#!/usr/bin/python3
""" module that writes a new file"""


def write_file(filename="", text=""):
    """ wrting to the file and settingin utf8"""
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
