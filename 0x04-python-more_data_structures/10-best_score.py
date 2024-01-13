#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        biggest_key = max(a_dictionary.items(), key=lambda a: a[1])[0]
        return biggest_key
    return None
