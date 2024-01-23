#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count_ = 0
    try:
        for i in range(x):
            if type(my_list[i]) is int:
                print("{:d}".format(my_list[i]), end="")
                count_ += 1
        print()
        return count_
    except (IndexError, ValueError, TypeError):
        print()
        return count_
