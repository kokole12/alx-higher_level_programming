#!/usr/bin/python3
""" Declears a rectanle class"""

class Rectangle:
    """ initializing the values for the rectangle"""
    number_of_instances = 0
    print_symbol = "#"

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
        Rectangle.number_of_instances += 1
    
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
                try:
                    rectangle += str(self.print_symbol)
                except Exception:
                    rectangle += type(self).print_symbol
            if column < self.__height - 1:
                rectangle += "/n"
        return (rectangle)

    def __repr__(self):
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """ prints a message for every object that is deleted"""
        print("Bye rectangle...")
    
    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
