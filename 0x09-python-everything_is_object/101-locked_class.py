#!/usr/bin/python3
class LockedClass:
    def __setattr__(self, name, value):
        if name != "first_name":
            raise AttributeError("'LockedClass' object has no attribute '{}'".format(name))
        else:
            self.__dict__[name] = value
