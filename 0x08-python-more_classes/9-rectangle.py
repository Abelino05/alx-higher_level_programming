#!/usr/bin/python3
"""Class that defines a rectangle based on 1-rectangle.py"""


class Rectangle:
    """Definition of a rectangle
    Attribute:
    width: Width of the rectangle
    height: Height of the rectangle
    """

    number_of_instances = 0
    print_symbol = '#'

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
        """Prints the rectangle with the character # or any"""
        st = ''
        if type(self.print_symbol) is not str:
            self.print_symbol = str(self.print_symbol)
        if self.__height == 0 or self.__width == 0:
            return st
        for i in range(self.__height):
            for j in range(self.__width):
                st += str(self.print_symbol)
                if j == self.__width - 1:
                    st += '\n'
        return st

    def __repr__(self):
        """Returns a string representation of the object"""
        return 'Rectangle(' + str(self.__width) + ', ' + \
            str(self.__height) + ')'

    def __del__(self):
        """Prints the message 'Bye rectangle' if an instance is deleted"""
        type(self).number_of_instances -= 1
        print('Bye rectangle...')

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the biggest rectangle based on area"""
        if isinstance(rect_1, Rectangle) is not True:
            raise TypeError('rect_1 must be an instance of Rectangle')
        if isinstance(rect_2, Rectangle) is not True:
            raise TypeError('rect_2 must be an instance of Rectangle')
        if Rectangle.area(rect_1) > Rectangle.area(rect_2):
            return rect_1
        elif Rectangle.area(rect_2) > Rectangle.area(rect_1):
            return rect_2
        else:
            return rect_1

    @classmethod
    def square(cls, size=0):
        """Returns a new rectangle"""
        return Rectangle(size, size)
