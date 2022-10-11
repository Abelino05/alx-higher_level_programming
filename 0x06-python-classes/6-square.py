#!/usr/bin/python3
"""This module contains class square"""


class Square:
    """ Calculate the square of a given size"""
    def __init__(self, size=0, position=(0, 0)):
        """The constructor:
        Attribute:
            size: int parameter
        """
        self.__size = int(size)
        self.__position = position

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

    @property
    def position(self):
        """return the position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the position"""
        if type(value) != tuple:
            raise TypeError('position must be a tuple of 2 positive integers')
        elif len(value) != 2 or type(value[0]) != int or type(value[1]) != int:
            raise TypeError('position must be a tuple of 2 positive integers')
        elif value[0] < 0 or value[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        else:
            self.__position = value

    def my_print(self):
        """Prints in stdout the square"""
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")
