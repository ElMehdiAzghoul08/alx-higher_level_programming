#!/usr/bin/python3
def uppercase(str):
    for character in str:
        if 'a' <= str <= 'z':
            new_str += chr(ord(character)) - ord('a') + ord('A')
            print(f"{new_str}".format(new_str))
    else:
        return str
