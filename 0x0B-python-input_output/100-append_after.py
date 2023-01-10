#!/usr/bin/python3
""" module for text insertion in a text file after search"""


def append_after(filename="", search_string="", new_string=""):
    """ inserts the string after a line containing the given string"""
    text = ""
    with open(filename) as f:
        for line in f:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, 'w') as w:
        w.write(text)
