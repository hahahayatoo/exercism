#!/usr/bin/python3 -V
# -*- coding: utf-8 -*-

SUBLIST = "A is a sublist of B"
SUPERLIST = "A is a superlist of B"
EQUAL = "A is equal to B"
UNEQUAL = "A is not a superlist of, sublist of or equal to B"

def check_lists(l1, l2):
    if len(l1) == len(l2):
        if check(l1, l2):
            return EQUAL
        else:
            return UNEQUAL
    elif len(l1) < len(l2):
        if check(l1, l2):
            return SUBLIST
        else:
            return UNEQUAL
    else:
        if check(l2, l1):
            return SUPERLIST
        else:
            return UNEQUAL

def check(x, y):
    for y_i in range(y.count(x[0])):
        y_s = y.index(x[0])
        for i,v in enumerate(x):
            if y[y_s+i] != v:
                y = y[y_s+1:]
                break
        else:
            return(True)
    else:
        return(False)
