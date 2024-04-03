#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return my_list

    modif_list = my_list.copy()
    modif_list[idx] = element
    return modif_list
