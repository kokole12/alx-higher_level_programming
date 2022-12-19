#!/usr/bin/python3
safe_print_integer = __import__('1-safe_print_integer').safe_print_integer

value = 89
has_been_printed = safe_print_integer(value)
if not has_been_printed:
    print(f'{value} is not a number')
value = -89
has_been_printed = safe_print_integer(value)
if not has_been_printed:
    print(f'{value} is not a number')
value = "school"
has_been_printed = safe_print_integer(value)
if not has_been_printed:
    print(f'{value} is not a number')
