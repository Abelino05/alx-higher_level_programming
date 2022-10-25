#!/usr/bin/python3
"""
Returns the list of available attributes and methods
"""


def lookup(obj):
    """List of available attributes and methods of an object
    Args:
        obj: object
    Returns:
        list: list of attributes and methods
    """
    return (dir(obj))
