#!/usr/bin/python3
"""Defines an inherited list class MyList."""


class MyList(list):
    """class MyList that inherits from list"""
    def print_sorted(self):
        """prints the list, but sorted (ascending sort)"""
        print(sorted(self))
