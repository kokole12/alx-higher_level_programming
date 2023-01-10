#!/usr/bin/python3
lookup = __import__('0-lookup').lookup

class MyClass(object):
    pass

class MyClass2(object):
    my_attr1 = 3
    def my_math(self):
        pass

print(lookup(MyClass))
print(lookup(MyClass2))
print(lookup(int))