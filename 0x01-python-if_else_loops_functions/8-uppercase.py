#!/usr/bin/python3
def uppercase(str):
    for character in str:
        if "a" <= str <= "z":
            print(chr(ord(character))) - ord('a') + ord('A')
    else:
        return print(str, end="")
