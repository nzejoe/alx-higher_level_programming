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