#!/usr/bin/python3
"""Class that define a rectangle"""


class Rectangle:
    """Class that define a rectangle.
    width: define the width o the rectangle
    height: define the height of the rectangle
    """
    def __init__(self, width=0, height=0):
        """The constructor"""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Gets the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle"""
        if isinstance(value, int) is not True:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ gets the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle"""
        if isinstance(value, int) is not True:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__height = value
