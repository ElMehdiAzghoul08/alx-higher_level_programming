#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        count_ = 0
        for i in range(x):
            print("{}".format(my_list[i]), end="")
            count_ += 1
        print()
        return count_
    except IndexError:
            print()
            return count_
