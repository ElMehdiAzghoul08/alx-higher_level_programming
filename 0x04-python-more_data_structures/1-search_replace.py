#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = list(map(lambda a: replace if a == search else a, my_list))
    return new_list
