"""double_add5.py
author:Chase Lewis
created: September 2017
CSCI-141"""

import math

def print_sequence_rec(start, count):
    """print_sequence_rec recursively generates the sequence from the start value"""
    if count < 0:
        pass
    else:
        print (start * 2 + 5)
        print_sequence_rec(start * 2 + 5, count - 1)

def print_sequence_iter(start, count):
    """print_sequence_iter iterativey generates the sequence from the start value"""
    while count > 0:
                print (start * 2 + 5)
                start = start * 2 + 5
                count = count - 1
    
                
def find_start_forward(goal, count):
    """find_start_forward iteratively searches for a value to start the sequence to be be greater than or equal to the goal"""
    start = 0
    x = 0
    c = count
    while goal > 0:
        while count > 0:
            start = start * 2 + 5
            count -= 1
            if start >= goal:
                print(x)
                return 
        if start < goal:
            count = c
            x += 1
            start = x

def find_back_limit_rec(nbr, count):
    """find_back_limit_rec recursively searches backward from nbr to find smallest value whose n value will be greater than or equal to nbr"""
    if count < 0:
        pass
    else: 
        find_back_limit_rec((math.ceil(nbr - 5) / 2), count - 1)
    if count == 0:
        print (math.ceil(nbr))
        
        
        

def find_back_limit_iter(nbr, count):
    """find_back_limit_iter recursively searches backward from nbr to find smallest value whose n value will be greater than or equal to nbr"""
    start = nbr
    while count > 0:
        start= math.ceil ((start - 5) / 2) 
        count -= 1
    print(start)
             

def test_function():
    """test_function test all of the functions with values"""
    print_sequence_rec(1, 2)
    print_sequence_rec(2,5)
    print_sequence_rec(3,2)
    print_sequence_iter(2, 5)
    print_sequence_iter(1, 1)
    print_sequence_iter(3, 3)
    find_start_forward(7, 3)
    find_start_forward(100, 1)
    find_start_forward(100, 3)
    find_back_limit_rec(1000, 3)
    find_back_limit_rec(500, 2)
    find_back_limit_rec(700, 4)
    find_back_limit_iter(1003, 3)
    find_back_limit_iter(4194299, 3)
    find_back_limit_iter(503, 2)

test_function()
print ("Close Windon When Finished")
    











        
        
    
    





