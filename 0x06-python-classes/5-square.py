#!/usr/bin/python3
"""This module contains class square"""


class Square:
    """ Calculate the square of a given size"""
    def __init__(self, size=0):
        """The constructor:
        Attribute:
            size: int parameter
        """
        self.__size = int(size)

    def area(self):
        """Calculate the square."""
        return self.__size**2

    @property
    def size(self):
        """return square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size value"""
        if isinstance(value, int) is not True:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def my_print(self):
        """Prints in stdout the square"""
        for i in range(self.__size):
            if self.__size == 0:
                print(' ', end='\n')
            else:
                print('#'*self.__size)
