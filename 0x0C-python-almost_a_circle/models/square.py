#!/usr/bin/python3

"""
Square Class Module that inherits from Rectangle:
Inits superclass' id, width (as size), height (as size), x, y
Class constructor: __init__(self, size, x=0, y=0, id=None)
Contains public attribute size
Contain public method of:
update(*args, **kwargs)
to_dictionary(self)
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Defines Square class that inherits from Rectangle.
    Inherited attributes of:
        id (Base), __width, __height, __x & __y
    Inherited methods of:
        Base.init(self, id=None);
        Rectangle.init(self, width, height, x=0, y=0, id=None);
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize a Square instance.
        Args:
            size (int): Size of the square.
            x (int, optional): X coordinate. Defaults to 0.
            y (int, optional): Y coordinate. Defaults to 0.
            id (int, optional): ID of the square. Defaults to None.
        """
        # call superclass constructor with all parameters
        super().__init__(size, size, x, y, id)