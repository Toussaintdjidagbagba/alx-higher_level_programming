#!/usr/bin/python3
def uniq_add(my_list=[]):
    nouveau = set(my_list)
    resultat = 0
    for i in nouveau:
        resultat += i
    return resultat
