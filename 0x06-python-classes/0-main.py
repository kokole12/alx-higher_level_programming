#!/usr/bin/python3
square = __import__('0-square').square

my_square = square()
print(type(my_square))
print(my_square.__dict__)
