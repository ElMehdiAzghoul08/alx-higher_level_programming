#!/usr/bin/python3

"""Defines class Student"""


class Student:
    """Represent Student class"""

    def __init__(self, first_name, last_name, age):
        """Initialize new Student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """to_json function"""
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
