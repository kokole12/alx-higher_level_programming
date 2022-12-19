#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count  = 0
    for n in range(x):
        try:
            print("{:d}".format(my_list[n]), end="")
            count = count + 1
        except (IndexError, ValueError):
            pass
    print()
    return count
