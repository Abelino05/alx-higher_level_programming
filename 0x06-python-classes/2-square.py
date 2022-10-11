#!/usr/bin/python3
"""This module contains square class"""


class Square:
    """Square class with:
    .Private instance attribute: size
    .Instantiation with optional size
    """
    def __init__(self, size=0):
        """Initialize attributes"""
        self.__size = int(size)
        if isinstance(size, int) is not True:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
