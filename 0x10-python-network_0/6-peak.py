#!/usr/bin/python3
""" fiind the peak value in a list"""

def find_peak(list_of_inegers):
    if len(list_of_inegers) == 0:
        return "None"
    list_of_inegers.sort()
    return list_of_inegers[-1]
