#!/usr/bin/python3
def islower(c):
    if ord("a") <= ord(c) <= ord("z"):
        print("{:c} is lower".format(c))
        return True
    else:
        print("{:c} is upper".format(c))
        return False
