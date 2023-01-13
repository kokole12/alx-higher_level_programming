#!/usr/bin/python3
""" 6-main"""
from models.rectangle import Rectangle

if __name__ == "__main__":

    r1 = Rectangle(2, 3, 2, 2)
    r1.display()

    print("---")

    r1 = Rectangle(3, 2, 1, 0)
    r1.display()
