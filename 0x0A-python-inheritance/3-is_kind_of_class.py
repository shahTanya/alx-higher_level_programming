#!/usr/bin/python3
"""Defines a class and inherited class-checking function"""


def is_kind_of_class(obj, a_class):
    """Check if an object is an instance or inherited instance of a class
    Args:
        obj - The object to check.
        a_class - class to match the type of obj to
    Return:
        True - object is an instance of,
        False - otherwise
    """
    if isinstance(obj, a_class):
        return True
    return False
