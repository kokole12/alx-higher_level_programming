#!/usr/bin/python3
add_integer = __import__('0-add_integer').add_integer

print(add_integer(2, 8))
print(add_integer(10, -2))
try:
    print(add_integer("a", 6))
except Exception as e:
    print(e)