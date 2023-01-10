#!/usr/bin/python3
""" inherits from base geometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ initializing the attrbutes for the rectangle"""
    def __init__(self, width, height):
        super().__init__()
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """ calcutes the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self) -> str:
        """ prints the string representation of the rectangle object"""
        string = "[" + str(self.__class__.__name__) + "]"
        string += str(self.__width) + "/" + str(self.__height)
        return string
