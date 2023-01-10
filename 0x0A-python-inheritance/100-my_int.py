#!/usr/bin/python3
""" the module defines a class myInt that inherits from inherits from int"""


class MyInt(int):
    """ int operators == and != inverted"""

    def __eq__(self, value):
        "overrides the == operator"
        return self.real != value

    def __neg__(self, value):
        """ overides the != operator with == behavior"""
        return self.real == value
