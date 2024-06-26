#!/usr/bin/python3

"""rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class"""

    def __init__(self, size):
        """New square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
