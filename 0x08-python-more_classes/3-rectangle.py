#!/usr/bin/python3
""" Declears a rectanle class"""


class Rectangle:
    """ initializing the values for the rectangle"""

    def __init__(self, width=0, height=0):
        """
        Args:
            width: the value for width
            height: the value for the height
        Raises:
            TypeError: if the size is not an integer
            ValueError: if the size is less than 0
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """ retrieves the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """ Sets the value for the width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ retrieves the value for the height"""
        return self.__height

    @height.setter
    def height(self, value):
        "sets and checks value for height"
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ calculates the value for the area"""
        return (self.__width * self.__height)

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self) -> str:
        " prints the diagram for the rectangler using #"
        if self.__width == 0 or self.__height == 0:
            return ('')
        rectangle = ""
        for column in range(self.__height):
            for row in range(self.__width):
                rectangle += "#"
            if column < self.__height - 1:
                rectangle += '\n'
        return (rectangle)
