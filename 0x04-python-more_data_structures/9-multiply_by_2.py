#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    nouveau = {}
    for i in a_dictionary:
        nouveau[i] = a_dictionary[i] * 2
    return nouveau
