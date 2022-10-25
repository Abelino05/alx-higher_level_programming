#!/usr/bin/python3
"""
Verifie the instance of an object
"""


def is_same_class(obj, a_class):
    """
    Verify if the object is an instance of the specified class
    Args:
        obj: object
        a_class:specified class
    Returns:
        True: if the object is an instance of the class
        False: if not
    """
    if type(obj) == a_class:
        return True
    else:
        return False
