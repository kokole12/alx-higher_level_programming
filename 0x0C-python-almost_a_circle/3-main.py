#!/usr/bin/python3
""" 3-main """
from models.rectangle import Rectangle

if __name__ == "__main__":

    r1 = Rectangle(3, 2)
    print(r1.area())

    r1 = Rectangle(2, 10)
    print(r1.area())

    r1 = Rectangle(8, 7, 0, 0, 12)
    print(r1.area())
