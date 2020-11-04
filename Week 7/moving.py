"""moving.py
author: Chase Lewis
created: October 2017
CSCI-141"""

from rit_lib import *

box = struct_type("Box", (int, "size"), (list, "items"), (int, "capacity"))

item = struct_type("Item", (str, "name"), (int, "weight"), (bool, "added"))



def read(filename):
    """reads the filename and turns the file in lists of items and boxes"""
    fd = open(filename)
    boxes = fd.readline().split()
    blist = []
    for i in boxes:
        blist.append(box(int(i), [], 0))
    item_list = []
    for line in fd:
        info = line.split()
        item_list.append(item((info[0]), int(info[1]), False ))
    fd.close()
    return blist, item_list

def getweight(item):
    """returns the item weight of the struct type"""
    return item.weight

def box_weight(box):
    """returns the box weihgt of the struct type"""
    return box.size




def roomiest(blist, item_list):
    """puts items into boxes based on which one has the most room"""
    blist = sorted(blist, key=box_weight, reverse=True)
    item_list = sorted(item_list, key=getweight, reverse=True)
    emptylist = []
    n = 1
    for item in item_list:
        blist.sort( key = box_weight, reverse = True)
        for box in blist:
            if item.weight <= box.size - box.capacity:
                box.capacity += item.weight
                box.items.append(item)
                item.added = True
                break
    for item in item_list:
        if item.added == False:
            emptylist.append(item)
    if emptylist == []:
        print ("All items succesfully packed into boxes")
    else:
        print ("Unable to pack all items!")
    for box in blist:
        print ("Box" , n , "of weight capacity" , box.size , "contains:" )
        n += 1
        for items in box.items:
            print (items.name + " of weight" , items.weight)
    for i in emptylist:
        if emptylist != []:
            print(item.name + " of weight" , item.weight , "got left behind.")

def tightestFit(blist, item_list):
    """puts items into the box with the least amount of room."""
    blist = sorted(blist, key=box_weight)
    item_list = sorted(item_list, key=getweight, reverse=True)
    emptylist = []
    n = 1
    for item in item_list:
        blist.sort(key=box_weight)
        for box in blist:
            if item.weight <= box.size - box.capacity:
                box.capacity += item.weight
                box.items.append(item)
                item.added = True
                break
    for item in item_list:
        if item.added == False:
            emptylist.append(item)
    if emptylist == []:
        print("All items succesfully packed into boxes")
    else:
        print("Unable to pack all items!")
    for box in blist:
        print("Box", n, "of weight capacity", box.size, "contains:")
        n += 1
        for items in box.items:
            print(items.name + " of weight", items.weight)
    for i in emptylist:
        if emptylist != []:
            print(item.name + " of weight", item.weight, "got left behind.")

def OneBox(item_list, blist):
    """puts items in the box one box at a time"""
    emptylist = []
    n = 1
    item_list = sorted(item_list, key=getweight, reverse=True)
    for item in item_list:
        for box in blist:
            if item <= box.size - box.capapcity:
                box.capacity += item.weight
                box.items.append(item)
                break
    for item in item_list:
        if item.added == False:
            emptylist.append(item)
    if emptylist == []:
        print("All items succesfully packed into boxes")
    else:
        print("Unable to pack all items!")
    for box in range(blist):
        print("Box", n, "of weight capacity", box.size, "contains:")
        n += 1
        for items in box.items:
            print(items.name + " of weight", items.weight)
    for i in emptylist:
        if emptylist != []:
            print(item.name + " of weight", item.weight, "got left behind.")



def main():
    """runs all of the greedy functions"""
    filename = input("Enter Filename: ")
    blist, item_list = read(filename)
#    print (roomiest(blist, item_list))
#    print (tightestFit(blist, item_list))
#    print (OneBox(blist, item_list))


                   

main()