"""
This exercise stub and the test suite contain several enumerated constants.

Enumerated constants can be done with a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = 0
SUPERLIST = 1
EQUAL = 2
UNEQUAL = 3


def sublist(list_one: list[int], list_two: list[int]):

    if (list_one == list_two):
        return EQUAL
    elif (is_sub(list_one, list_two)):
        return SUBLIST
    elif (is_sub(list_two, list_one)):
        return SUPERLIST
    return UNEQUAL


def is_sub(short_list: list[int], large_list: list[int]):
    for i in range(len(large_list) - len(short_list) + 1):
        if large_list[i:i+len(short_list)] == short_list:
            return True
    return False
