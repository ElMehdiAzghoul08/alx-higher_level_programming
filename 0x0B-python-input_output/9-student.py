#!/usr/bin/python3

"""Defines class Student"""


class Student:
    """Represents a student class"""

    def __init__(self, first_name, last_name, age):
        """Initialize new Student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """to_json function"""
        return self.__dict__
