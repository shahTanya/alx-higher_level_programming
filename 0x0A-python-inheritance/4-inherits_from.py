#!/usr/bin/python3
"""Defines an inherited class-checking function."""


def inherits_from(obj, a_class):
    """Checks if an object is an inherited instance of a class.
    Args:
        obj - object to check
        a_class - class to match the type of obj to
    Return:
        True - object is an instance of a class that inherited
            (directly or indirectly) from the specified class
        False - otherwise
        """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
