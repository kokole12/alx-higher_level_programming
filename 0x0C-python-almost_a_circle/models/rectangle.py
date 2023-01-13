#!/usr/bin/python3
""" class rectangle inherits from Base"""
from models.base import Base


class Rectangle(Base):
    """ initializing the constructor"""

    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ returning the value for the width"""

        return self.__width

    @width.setter
    def width(self, value):
        """ setting and checking the value for height"""

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ return the value for the height"""

        return self.__height

    @height.setter
    def height(self, value):
        """ setting and checking the value for height"""

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ returning the value for x"""

        return self.__x

    @x.setter
    def x(self, value):
        """ setting and checking the value for x"""

        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ returning the value for y"""

        return self.__y

    @y.setter
    def y(self, value):
        """ checking the values for y"""

        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ calculating the area of the rectangle"""

        return (self.__width *  self.__height)

    def display(self):
        """ displaying the rectangle using #"""
        for y in range(self.y):
            print("")
        for row in range(self.height):
            for x in range(self.x):
                print(" ", end="")
            for column in range(self.width):
                print("#", end="")
            print()

    def __str__(self):
        """ defines a format that will return the object as a string"""

        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"

    def update(self, *args, **kwargs):
        """ updating the attritbutes of rectangle class"""

        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.width = arg
                elif a == 2:
                    self.height = arg
                elif a ==3:
                    self.x == arg
                elif a == 4:
                    self.y = arg
                a +=1
        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = v
                elif k == "width":
                    self.width = v
                elif k == "height":
                    self.height = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """ dictionary representation of the object"""

        obj_dict = {'id': self.id,  'x': self.x,  'y': self.y,\
            'height': self.height, 'width': self.width}
        return obj_dict
