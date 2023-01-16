#!/usr/bin/python3
""" Initializing a class base"""
import json
import os


class Base:
    """ class variable to keep track of the instances of base"""

    __nd_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nd_objects += 1
            self.id = Base.__nd_objects

    @staticmethod
    def to_json_string(list_dictinaries):
        """ returns a json string representation of the dictinaries"""

        if list_dictinaries is None or list_dictinaries == []:
            return '[]'
        return json.dumps(list_dictinaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ save json representation of files"""

        file_name = cls.__name__ + ".json"
        with open(file_name, 'w') as f:
            if list_objs is None:
                f.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                f.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """ returns the json string from json"""

        json_string_list = []
        if json_string is None and json_string != '':
            return '[]'
        json_string_list = json.loads(json_string)
        return json_string_list

    @classmethod
    def create(cls, **dictinary):
        """ retruns instances with all attributes set"""

        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)

        dummy.update(**dictinary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ returns the list of instances from files"""

        file_name = cls.__name__ + ".json"
        list_of_instances = []
        list_dictionaries = []

        if os.path.exists(file_name):
            with open(file_name, 'r') as f:
                mystr = f.read()
                list_dictionaries = cls.from_json_string(mystr)
                for dictionary in list_dictionaries:
                    list_of_instances.append(cls.create(**dictionary))
        return list_of_instances
