#!/usr/bin/python3
""" A module that contain is_same_class() method. """


def is_same_class(obj, a_class):
    """returns True if the object is exactly
        an instance of the specified class
        Args:
            obj(object)
            a_class(class)
        Return:
            true if object is anstance of the class.
    """
    if type(obj) == a_class:
        return True
    else:
        return False
