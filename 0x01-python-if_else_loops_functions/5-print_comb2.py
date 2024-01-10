#!/usr/bin/python3
for numbers in range(1, 100):
    print("{:02d}".format(numbers), end=", " if numbers < 99 else "\n")
