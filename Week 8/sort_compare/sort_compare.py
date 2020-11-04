"""sort_compare.py
author: Chase Lewis
created: October 2017
CSCI-141"""

import time
import random

def insertionSort( lst ):
   """
   insertionSort: List( A ) -> NoneType
      where A is totally ordered
      effect: modifies lst so that the elements are in order
   """
   for mark in range( len( lst )-1 ):
      insert( lst, mark )


def insert( lst, mark ):
   """
   insert: List( A ) * NatNum -> NoneType
      where A is totally ordered
      effect: moves the value just past the mark to its sorted position
   """
   for index in range( mark, -1, -1 ):
      if lst[index] > lst[index+1]:
         swap( lst, index, index+1 )
      else:
         return


def swap( lst, i, j ):
   """
   swap: List( A ) * NatNum * NatNum -> NoneType
      where A is totally ordered
      effect: swaps the values in lst at positions i and j
   """
   ( lst[i], lst[j] ) = ( lst[j], lst[i] )


def mergeSort(list):
    """
    mergeSort: List( A ) -> List( A )
       where A is totally ordered
    """
    if list == []:
        return []
    elif len(list) == 1:
        return list
    else:
        ( half1, half2 ) = split(list)
        return merge(mergeSort(half1), mergeSort(half2))


def split(list):
    """
    split: List( A ) -> Tuple( List( A ), List( A ) )
    """
    evens = []
    odds = []
    isEvenIndex = True
    for e in list:
        if isEvenIndex:
            evens.append(e)
        else:
            odds.append(e)
        isEvenIndex = not isEvenIndex
    return ( evens, odds )


def merge(sorted1, sorted2):
    """
    merge: List( A ) * List( A ) -> List( A )
    precondition: sorted1 and sorted2 are lists whose elements are in order
    """
    result = []
    index1 = 0
    index2 = 0
    while index1 < len(sorted1) and index2 < len(sorted2):
        if sorted1[index1] <= sorted2[index2]:
            result.append(sorted1[index1])
            index1 = index1 + 1
        else:
            result.append(sorted2[index2])
            index2 = index2 + 1
    if index1 < len(sorted1):
        result.extend(sorted1[index1:])
    elif index2 < len(sorted2):
        result.extend(sorted2[index2:])
    return result


def quicksort( list ):
    """
    quickSort: List( A ) -> List( A )
        where A is 'totally ordered'
    """
    if list == []:
        return []
    else:
        pivot = list[0]
        ( less, same, more ) = partition( pivot, list )
        return quicksort( less ) + same + quicksort( more )

def partition( pivot, L ):
    """
    partition: A * List( A ) -> Tuple( List( A ), List( A ), List( A ) )
        where A is totally ordered
    """
    ( less, same, more ) = ( [], [], [] )
    for e in L:
        if e < pivot:
            less.append( e )
        elif e > pivot:
            more.append( e )
        else:
            same.append( e )
    return ( less, same, more )

def test_quicksort():
    """This function will the test the quickSort algorithm and confirm that it's correct"""
    unsorted = [8,5,9,10,1]
    sorted = [1,5,8,9,10]
    quicksort(unsorted)
    if quicksort(unsorted) == sorted:
        print ("The quickSort algorithm works:)")


def test_insertionSort():
    """This function will the the insertionSort algorithm and confirms that it's correct """
    unsorted = [2,3,1]
    sorted = [1,2,3]
    insertionSort(unsorted)
    if unsorted == sorted:
        print ("The insertionSort algorithm works:)")

def test_mergeSort():
    """This function will test the mergeSort algorithm and confirm that it's correct"""
    unsorted = [8,5,9,10,1]
    sorted = [1,5,8,9,10]
    mergeSort(unsorted)
    if mergeSort(unsorted) == sorted:
        print("The mergeSort algorithm works:)")




def main():
    """main gets inputs for tests from the user. Creates a random list. Run each algorithm on a copy of that list, and
reports the size of the list; Report the time it took to sort the list; and Prevent further testing of the algorithm
 if the time exceeds 1 second."""
    test_quicksort()
    test_insertionSort()
    test_mergeSort()
    g = (int(input("What is the min possible value of an item in the list:"))) - 1
    n = (int(input("What is the max possible value of an item in the list:" ))) + 1
    q = int(input("Initial list size:"))
    t = int(input("What is the timeout (in seconds)?" ))
    list = random.sample(range(g - 1, n + 1), q)
    qslist = list[:]
    islist = list[:]
    mslist = list[:]
    (timequick, timeinsert, timemerge) = (0,0,0)
    while timequick < t and timeinsert < t or timeinsert < t and timemerge < t or timemerge < t and timequick < t:
        print ("Size:" + str(q))
        list = random.sample(range(g - 1, n + 1), q)
        qslist = list[:]
        islist = list[:]
        mslist = list[:]
        if timequick < t:
            startquick = time.time()
            quicksort(qslist)
            endquick =time.time()
            timequick = endquick - startquick
            print ("Quick Sort time is:" + str(endquick - startquick))
        if timeinsert < t:
            startinsert = time.time()
            insertionSort(islist)
            endinsert = time.time()
            timeinsert = (endinsert - startinsert)
            print("Insertion Sort time is:" + str(timeinsert))
        if timemerge < t:
            startmerge = time.time()
            mergeSort(mslist)
            endmerge = time.time()
            timemerge = endmerge - startmerge
            print("Merge Sort time is:" + str(endmerge - startmerge))
        q *= 10


main()
