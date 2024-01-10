#!/usr/bin/python3
def islower(c):
    for c in range(97, 122):
        print("{:d} is lower".format(c))
        return True
    else:
        print("{:d} is upper".format(c))
        return False
