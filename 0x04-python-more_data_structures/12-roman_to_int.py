#!/usr/bin/python3
def roman_to_int(roman_string):
    dicto = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    new_ro = 0
    for i in range(len(roman_string)):
        if i > 0 and dicto[roman_string[i]] > dicto[roman_string[i - 1]]:
            new_ro += dicto[roman_string[i]] - 2 * \
                        dicto[roman_string[i - 1]]
        else:
            new_ro += dicto[roman_string[i]]
    return new_ro
