#!/usr/bin/python3

"""
Base class Module inside the Models Python Package.
private class attribute __nb_objects = 0
class constructor: def __init__(self, id=None)::
if id is not None, assign the public instance attribute id
with this argument value - you can assume id is an integer
and you don’t need to test the type of it otherwise,
increment __nb_objects and assign the new value to
the public instance attribute id
Add static method def to_json_string(list_dictionaries):
that returns the JSON string representation of list_dictionaries.
Add class method def save_to_file(cls, list_objs):
that writes the JSON string representation of list_objs to a file.
Add static method def from_json_string(json_string):
that returns the list of the JSON string representation json_string:
Add class method def create(cls, **dictionary):
that returns an instance with all attributes already set:
Add class method def load_from_file(cls): that returns a list of instances:
Add the class methods def save_to_file_csv(cls, list_objs):
and def load_from_file_csv(cls): that serializes and deserializes in CSV:
Has the same behavior as the JSON serialization/deserialization
Format of the CSV:
    Rectangle: <id>,<width>,<height>,<x>,<y>
    Square: <id>,<size>,<x>,<y>
Add the static method def draw(list_rectangles, list_squares):
that opens a window and draws all the Rectangles and Squares:
"""

import json


class Base:
    """
    Base class to manage id attribute in all future classes
    and to avoid duplicating the same code
    (by extension, same bugs)
    """
    __nb_objects = 0  # private class attribute

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            # increment __nb_objects & assign the new value to the id attribute
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Method to return JSON string representation - list of dictionaries.
        """
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write JSON string representation into a file.
        Args:
            cls (class): The class (e.g., Rectagle, Square, etc).
            list_objs (list of instances): instances that inherits from Base.
        """
        json_list = []
        if list_objs is not None:
            for obj in list_objs:
                json_list.append(cls.to_dictionary(obj))

        filename = '{}.json'.format(cls.__name__)
        with open(filename, 'w') as my_file:
            my_file.write(cls.to_json_string(json_list))

    @staticmethod
    def from_json_string(json_string):
        """Return the list represented by a JSON string.
        Args:
            json_string (str): JSON string representing a list of dictionaries.
        Returns:
            list: The list of dictionaries represented by the JSON string.
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)