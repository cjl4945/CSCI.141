"""test_link_sort.py
author: Chase Lewis
created: November 2017
CSCI-141"""

from link_sort import *





def read_file(filename):
    """reads a file and puts integers into a list and turns it into nodes"""
    p = None
    fd = open(filename)
    for c in fd:
        c = c.strip()
        p = Node(int(c), p)
    return p



def main():
    """declares the order of how the functions should be ran"""
    filename = input("Enter Filename:")
    if filename == "":
        pass
    else:
        print ("unsorted: " , read_file(filename))
        lns = read_file(filename)
        print ("sorted: ", link_sort(lns))
        sorted = link_sort(lns)
        print ("pretty print original: ", pretty_print(lns))
        print ("pretty print sorted: ", pretty_print_sorted(sorted))
main()