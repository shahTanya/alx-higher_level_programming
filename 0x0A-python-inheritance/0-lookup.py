#!/usr/bin/python3
"""returns the list of available attributes and methods"""


def lookup(obj):
    """Return a list of an object's available attributes."""
    return(dir(obj))
