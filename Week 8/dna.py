"""dna.py
Author: Chase Lewis
Created: November 2017
CSCI-141"""

from linked_code import *

def convert_to_nodes(DNA):
    """this function converts a list of strings into nodes"""
    if len(DNA) <= 0:
        return None
    else:
        return Node(DNA[0],convert_to_nodes(DNA[1:]))

def convert_to_string(dna_seq):
    """this functions converts nodes into strings"""
    """puts elements of a linked node sequence into a list """
    s = ""
    if dna_seq == None:
        return ""
    else:
        s += str(dna_seq.value)
        dna_seq = dna_seq.rest
        return s + convert_to_string(dna_seq)


def is_match(dna_seq1,dna_seq2):
    """this function determines if the two dna strands are a match"""
    if dna_seq1 == None and dna_seq2 == None:
        return True
    elif dna_seq1 == None or dna_seq2 == None:
        return False
    else:
        if dna_seq1.value == dna_seq2.value:
            return is_match(dna_seq1.rest, dna_seq2.rest)
        else:
            return False

def is_pairing(dna_seq1, dna_seq2):
    """this function determines if the two dna strands are pairs of each other"""
    if dna_seq1 == None and dna_seq2 == None:
        return True
    if lengthIter(dna_seq1) != lengthIter(dna_seq2):
        return False
    if dna_seq1 == None or dna_seq2 == None:
        return False
    else:
        if dna_seq1.value == "A" and dna_seq2.value == "T":
            return is_pairing(dna_seq1.rest, dna_seq2.rest)
        if dna_seq1.value == "T" and dna_seq2.value == "A":
            return is_pairing(dna_seq1.rest, dna_seq2.rest)
        if dna_seq1.value == "G" and dna_seq2.value == "C":
            return is_pairing(dna_seq1.rest, dna_seq2.rest)
        if dna_seq1.value == "C" and dna_seq2.value == "G":
            return is_pairing(dna_seq1.rest, dna_seq2.rest)
        else:
            return False

def is_palindrome(dna_seq):
    """this fuctions determines if the dna strand is a palindrome"""
    if dna_seq == None:
        return True
    if lengthIter(dna_seq) == 1:
        return True
    else:
        if dna_seq.value == reverseIter(dna_seq).value:
            dna_seq = dna_seq.rest
            return is_palindrome(dna_seq.rest)
        else:
            return False

def substitution(dna_seq, idx, base):
    """this function substitutes a base with a new base"""
    if idx > lengthIter(dna_seq) - 1:
        raise IndexError("Index out of range")
    if idx == 0:
        #removeAt(0,dna_seq)
        #insertAt(0, base, dna_seq)
        return Node(base, dna_seq.rest)
    if idx > 0:
        return Node(dna_seq.value, substitution(dna_seq.rest, idx -1, base))




def insertion(dna_seq1, dna_seq2, dna_seq3):
    """this function inserts a base in the dna strand without removing any bases"""
    if dna_seq3 == 0:
        return cat(dna_seq2, dna_seq1)
    elif dna_seq1 == None:
        raise IndexError("Invalid Insertion index")
    else:
        return Node(dna_seq1.value, insertion(dna_seq1.rest, dna_seq2, dna_seq3 - 1))

def deletion(dna_seq1, idx, segment_size):
    """"this function deletes a specified segment_size of the node"""
    if segment_size == 0:
        return dna_seq1
    if dna_seq1 == None and (idx > 0 or segment_size > 0):
        raise IndexError ("Both Index and segment size are out of range")
    else:
        if idx > 0:
             return Node(dna_seq1.value, deletion(dna_seq1.rest, idx - 1, segment_size))
        if idx == 0:
            return deletion(dna_seq1.rest, idx, segment_size - 1)

def duplication(dna_seq, idx, segment_size):
    """This function duplicates a specified segment of elements from dna_seq and concatenates them on to a node after the segment that was copied"""
    copy1 = dna_seq
    copy2 = dna_seq
    if segment_size == 0:
        return dna_seq
    elif idx + segment_size <= lengthIter(copy2):
        x = deletion(copy2, 0, idx)
        y = deletion(x,segment_size, lengthIter(x) - segment_size)
        return insertion(copy1, y, idx)
    else:
        raise IndexError("Error")


        
    
    
    
