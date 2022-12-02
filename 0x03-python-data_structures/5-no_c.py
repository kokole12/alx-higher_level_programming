#!/usr/bin/python3
def no_c(my_string):
    update_str = ''
    for i in my_string:
        if i != 'c' and i != "C":
            update_str += i
    return update_str
