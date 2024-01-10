#!/usr/bin/python3
def islower(c):
    if 97 <= ord(c) <= 122:
        print("{:d} is lower".format(c))
        return True
    else:
        print("{:d} is upper".format(c))
        return False
