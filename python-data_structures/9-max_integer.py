#!/usr/bin/python3

def max_integer(my_list=[]):
    if not my_list:
        return None
    else:
        trié = sorted(my_list)
        return trié[-1]
