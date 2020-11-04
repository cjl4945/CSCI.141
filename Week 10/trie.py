"""trie.py
author: Chase Lewis
created: November 2017
CSCI-141"""


from rit_lib import *

Trie = struct_type( "BinaryTree", ((NoneType, 'BinaryTree'), "left"), ( object, "value"),((NoneType, 'BinaryTree'), "right"))

def split(trie,x,y,idx):
    """The split funciton splits the x and y values into a subleaf after being called by the insert fucntion"""
    if x[idx] != y[idx]:
        if x[idx] == "0" and y[idx] == "1":
            trie.left = Trie(None,x,None)
            trie.right = Trie(None,y,None)
            return True
        else:
            trie.left = Trie(None, y, None)
            trie.right = Trie(None, x, None)
            return True

    else:
        if x[idx] == "0":
            trie.left = Trie(None, "", None)
            return split(trie.left,x,y, idx + 1)
        else:
            trie.right = Trie(None, "", None)
            return split(trie.right,x,y,idx + 1)

def insert(trie,x):
    """Insert calls the insert helper that has three parameters instead of two"""
    return (insert_helper(trie,x,0))

def insert_helper(trie,x,idx):
    """The insert function inserts a string into a non-empty trie, and returns either True or False indicating whether or not the insertion is succesful.
    It is a pre-condition"""
    if trie.value == "":
        if x[idx] == "0":
            if trie.left != None:
                return insert_helper(trie.left, x, idx + 1 )
            else:
                trie.left = Trie(None, x, None)
                return True
        else:
            if trie.right != None:
                return insert_helper(trie.right,x, idx + 1)
            else:
                trie.right = Trie(None, x, None)
                return True
    else:
        y = trie.value
        if x == y:
            return False
        else:
            trie.value = ""
            return split(trie, x,y,idx)



def trie_to_list(trie):
    """The trie to list function creates and returns a Python list of strings in trie in increasing order"""
    if trie == None:
        return []
    elif trie.left == None and trie.right == None:
        return [trie.value]
    else:
        return trie_to_list(trie.left) +  trie_to_list(trie.right)
    

def largest(trie):
    """The largest function returns the largest string in lexicographic order from teh set of strings stored in trie. It is a pre-conditon that
    trie is not empty"""
    if trie != None:
        if (trie.value == "" or trie.value == None) and trie.right == None:
            return largest(trie.left)
        elif (trie.value == "" or trie.value == None) and trie.right != None:
            return largest(trie.right)
        else:
            return trie.value
    else:
        return None





def smallest(trie):
    """The smallest function returns the smallest string in hexicographic order drom set of strings stored in trie. It is a
    pre-condition that trie is not empty"""
    if trie != None:
        if (trie.value == "" or trie.value == None) and trie.left == None:
            return smallest(trie.right)
        elif (trie.value == "" or trie.value == None) and trie.left != None:
            return smallest(trie.left)
        else:
            return trie.value
    else:
        return None


def search(trie, x):
    """The search function returns the string in trie that has the longest and closest prefix match with x."""
    if trie != None:
        if trie.left == None and trie.right == None:
            return trie.value
        else:
            if x[0] == "0":
                if trie.left == None:
                    return smallest(trie)
                else:
                    return search(trie.left, x[1:])
            else:
                if trie.right == None:
                    return smallest(trie)
                else:
                    return search(trie.right, x[1:])

    else:
        return None



        




def size(trie):
    """The size fucntion returns the number of strings stored in the trie"""
    count = 0
    lst = trie_to_list(trie)
    if lst == None:
        return 0
    else:
        return len(lst)



def height(trie):
    """THe height function calls the height helper with two parameters"""
    return height_helper(trie, 0)

def height_helper(trie, h):
    """The height helper funciton returns the height of the trie. Recall that the height of a trie is the maximum length of paths from the
    root of the trie to any leaf node"""
    if trie == None or (trie.left is None and trie.right is None ):
        return h
    else:
        return max(height_helper(trie.left, h + 1), height_helper(trie.right, h + 1))

