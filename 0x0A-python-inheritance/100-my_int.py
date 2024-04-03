#!/usr/bin/python3

"""MyInt"""


class MyInt(int):
    """MyInt class"""

    def __eq__(self, value):
        """__eq__ function"""
        return self.real != value

    def __ne__(self, value):
        """__ne__ function"""
        return self.real == value
