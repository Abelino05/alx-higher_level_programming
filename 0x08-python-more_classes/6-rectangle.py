#!/usr/bin/python3
"""Class that defines a rectangle based on 1-rectangle.py"""


class Rectangle:
    """Definition of a rectangle
    Attribute:
    width: Width of the rectangle
    height: Height of the rectangle
    """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initialize the object"""
        self.__width = width
        self.__height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """Retreive the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width value"""
        if isinstance(value, int) is not True:
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """Retreive the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height value"""
        if isinstance(value, int) is not True:
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """Returns the rectangle area"""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__width + self.__height) * 2

    def __str__(self):
        """Prints the rectangle with the character #"""
        str = ""
        if self.__height == 0 or self.__width == 0:
            return str
        for i in range(self.__height):
            for j in range(self.__width):
                str += '#'
                if j == self.__width - 1:
                    str += '\n'
        return str

    def __repr__(self):
        """Returns a string representation of the object"""
        return 'Rectangle(' + str(self.__width) + ', ' + \
            str(self.__height) + ')'

    def __del__(self):
        """Prints the message 'Bye rectangle' if an instance is deleted"""
        type(self).number_of_instances -= 1
        print('Bye rectangle...')
