#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if not my_list:
        return []
        new_list = [number % 2 == 0 for number in my_list]
        new_list.append(True)
    else:
        new_list.append(False)
    return new_list
