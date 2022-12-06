#!/usr/bin/python3
def unique_add(my_list=[]):
    num = 0
    for i in set(my_list):
        num += i
    return num
