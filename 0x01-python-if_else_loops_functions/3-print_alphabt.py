#!/usr/bin/python3
for letters in range(97, 123):
    if letters not in [101, 113]:
        print("{:c}".format(letters), end="")
