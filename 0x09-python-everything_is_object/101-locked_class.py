#!/usr/bin/python3
class LockedClass:
    """class named Locked class"""
    def __setattr__(self, name, value):
        """function setattr"""
        if name != "first_name":
            raise AttributeError("'LockedClass' object has no attribute '{}'".format(name))
        else:
            self.__dict__[name] = value
