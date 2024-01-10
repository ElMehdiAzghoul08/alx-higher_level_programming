#!/usr/bin/python3
def islower(c):
    if 97 <= ord(c) <= 122:
        print("{:c} is lower".format(c))
        return True
    else:
        print("{:c} is upper".format(c))
        return False
