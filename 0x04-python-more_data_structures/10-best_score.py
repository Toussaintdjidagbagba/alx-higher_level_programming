#!/usr/bin/python3
def best_score(a_dictionary):
    i = list(a_dictionary.keys())[0]
    j = a_dictionary[i]
    for p, m in a_dictionary.items():
        if m > j:
            j = m
            i = p
    return (i)
