"""link_sort.py
author: Chase Lewis
created: November 2017
CSCI-141"""

from linked_code import *




def find_minvalue(lns):
    """finds the minimum element of a linked node sequence"""
    pam = lns
    lil = lns.value
    while pam != None:
        if pam.value <= lil:
            lil = pam.value
            pam = pam.rest
        else:
            pam = pam.rest
    return lil
def link_sort(lns):
    """sorted a linked node sequence using selection sort"""
    sorted = None
    if lns == None:
        return lns
    else:
        while lns != None:
            m = find_minvalue(lns)
            lns = remove(m,lns)
            sorted = insertAt(0,m,sorted)
    return reverseTailRec(sorted)

def pretty_print_sorted(sorted):
    """puts elements of sorted linked node sequence into a normal list"""
    s = ""
    for i in range(lengthRec(sorted)):
        s += str(sorted.value) + ','
        sorted = sorted.rest
    return '[' + s[:-1] + ']'

def pretty_print(lns):
    """puts elements of a linked node sequence into a list """
    s = ""
    for i in range(lengthRec(lns)):
        s += str(lns.value) + ','
        lns = lns.rest
    return '[' + s[:-1] + ']'













