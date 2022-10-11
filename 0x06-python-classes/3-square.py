#!/usr/bin/python3
"""This module contains the class square"""


class Square:
    """A class defined by:
    .Private instance attribute: size
    .Instantiation with optional size
    .Public instance method: def area
    """
    def __init__(self, size=0):
        """Initiaize attributes"""
        self.__size = size
        if isinstance(size, int) is not True:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')

    def area(self):
        """Calculate the area"""
        return self.__size**2
