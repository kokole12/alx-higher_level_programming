#!/usr/bin/python3
""" module to help in reading files in python"""


def read_file(filename=""):
    """ prints the contents to output"""
    with open(filename, 'r', encoding='utf-8') as f:
        print(f.read(), end="")
