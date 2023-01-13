#!/usr/bin/python3
""" Square class inherits from Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Initializing the square constructor"""

    def __init__(self, size, x=0, y=0, id=None):
        self.size = size
        self.x = x
        self.y = y
        self.id = None
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ prints the instances of square as string"""

        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    @property
    def size(self):
        return self.__width

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
        self.__height = value

    def update(self, *args, **kwargs):
        """ updating the attributes of square class"""

        if args is not None and len(args) !=0:
            if len(args) >= 1:
                if type(args[0]) != int and args[0] is not None:
                    raise TypeError("id must be an integer")
                self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
        else:
            for k, v in kwargs.items():
                if k == "id":
                    if type(v) != int and v is not None:
                        raise TypeError("id must be an integer")
                    self.id = v
                    if k == "size":
                        self.size = v
                    if k == "x":
                        self.x = v
                    if k == "y":
                        self.y = v

    def to_dictionary(self):
        """ dictionary representation of the object"""

        obj_dictionary = {'id': self.id, 'x': self.x, 'size': self.size, 'y': self.y}
        return obj_dictionary

