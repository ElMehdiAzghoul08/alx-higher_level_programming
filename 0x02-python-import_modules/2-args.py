#!/usr/bin/python3
import sys
if __name__ == "__main__":
    arg = len(sys.argv) - 1  # to avoid counting the file name
    if arg < 1:
        print("0 arguments.")
    elif arg == 0:
        print("1 arguments:")
    else:
        print("{} arguments:".format(arg))
    for i in range(arg):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
