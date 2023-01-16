#!/usr/bin/python3
""" 18-main.py"""
from models.rectangle import Rectangle
from models.square import Square

if __name__ == "__main__":

    r1 = Rectangle(10, 7, 2, 8)
    r2 = Rectangle(2, 4)
    list_rectangles_input = [r1, r2]

    Rectangle.save_to_file(list_rectangles_input)

    list_rectangles_output = Rectangle.load_from_file()

    for rec in list_rectangles_input:
        print("[{}] {}".format(id(rec), rec))

    print('---')
    print('---')

    s1 = Square(5)
    s2 = Square(7, 9, 1)
    list_square_input = [s1, s2]

    Square.save_to_file(list_square_input)

    list_square_output = Square.load_from_file()

    for square in list_rectangles_input:
        print("[{}] {}".format(id(rec), rec))

    print('---')

    for square in list_square_output:
        print("[{}] {}".format(id(rec), rec))
