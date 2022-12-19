#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """Diving elements in two lists
    arguments of the functions are:-
            my_list_1
            my_list_2
            list_lenght
    returns a new list with values after division
    """
    new_list = []

    for i in range(0, list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            result = 0
        except ZeroDivisionError:
            print("division by 0")
            result = 0
        except IndexError:
            print("out of range")
            result = 0
        finally:
            new_list.append(result)
    return (new_list)
