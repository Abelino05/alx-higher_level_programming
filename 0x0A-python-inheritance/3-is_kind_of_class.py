#!/usr/bin/python3
"""
Verify if is an instance or the object is an instance
"""


def is_kind_of_class(obj, a_class):
    """
    Verify if is an instance or the object is an instance
    Args:
        obj: an object
        a_class: a class
    Returns: Bool
    """
    return isinstance(obj, a_class)
