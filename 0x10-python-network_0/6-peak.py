#!/usr/bin/python3
"""function that finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """function finc_peak"""
    if not list_of_integers:
        return None
    lt = 0
    rt = len(list_of_integers) - 1

    while lt < rt:
        ctr = (lt + rt) // 2

        if list_of_integers[ctr] > list_of_integers[ctr + 1]:
            rt = ctr
        else:
            lt = ctr + 1

    return list_of_integers[lt]
