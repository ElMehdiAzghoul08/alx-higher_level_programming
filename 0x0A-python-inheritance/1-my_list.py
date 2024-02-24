#!/usr/bin/python3
""" module contain "MyList" class"""


class MyList(list):
    """A class MyList that inherets from list.
        Args:
        list(class): parent class.
    """
    def print_sorted(self):
        """ prints a list, sorted."""
        print(sorted(self))
