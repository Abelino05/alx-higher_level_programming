#!/usr/bin/python3
"""
Module 1-my_list
"""


class MyList(list):
    """
    Class inheriting from list
    """
    def print_sorted(self):
        """
        Prints a sorted list
        """
        print(sorted(self))
