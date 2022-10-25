#!/usr/bin/python3
"""
module: 4-inherits_from
"""


def inherits_from(obj, a_class):
    """
    The obj is an instance of a class that inherited (directly or indirectly)
    Args:
        obj: an object
        a_class: a class
    returns:
        None
    """
    return type(obj) != a_class and isinstance(obj, a_class)