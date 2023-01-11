#!/usr/bin/python3
def best_score(a_dictionary):
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None
    i = list(a_dictionary.keys())[0]
    j = a_dictionary[i]
    for p, m in a_dictionary.items():
        if m > j:
            j = m
            i = p
    return (i)
