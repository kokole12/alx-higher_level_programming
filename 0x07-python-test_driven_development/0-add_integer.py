#!/usr/python3
""" function that adds two intergers or floats"""


def add_integer(a, b=98):
    """ declaring the function for addition
    Args:
        a: first argument
        b: second argument
    Return:
    the value of sum of a and b

    Raises:
        TypeError if the argument is not integer or float
    """

    if type(a) not in [int, float]:
        raise TypeError("{} must be an integer".format(a))
    if type(b) not in [int, float]:
        raise TypeError("{} must be an integer".format(b))

    return (int(a) + int(b))
