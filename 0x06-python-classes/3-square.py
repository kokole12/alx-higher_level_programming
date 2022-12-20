#!/usr/bin/python3
# 2-square.py by Kokole ismail
""" Declares square"""


class Square:
    """ Initializing the class
    args:
        size - initialized to zero
    Raises:
        ValueError: if size is less than zero
        TypeError: if size if not an integer
    """

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size

    def area(self):
        """
        Calculate area of the square
        Returns: The square of the size
        """

        return (self.__size ** 2)
