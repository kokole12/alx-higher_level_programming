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

    @property
    def size(self):
        """ Retrieves the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """ Assigns value of size"""
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """
        Calculate area of the square
        Returns: The square of the size
        """

        return (self.__size ** 2)
