"""fruitfulFun.py
author:Chase Lewis
created: September 2017
CSCI-141"""

def sumSquares(n):
    """sumSquares will give total of squares added together"""
    if n == 0:
        return 0
    else:
        return n**2 + sumSquares(n-1)


def sumSquaresTest():
    """sumSquaresTest tests sumSquares and sumSquaresTR"""
    print(str(sumSquares(0)))
    print(str(sumSquares(1)))
    print(str(sumSquares(2)))
    print(str(sumSquares(3)))
    print(str(sumSquares(4)))
    print(str(sumSquares(5)))
    print(str(sumSquares(6)))
    print(str(sumSquaresTR(0)))
    print(str(sumSquaresTR(1)))
    print(str(sumSquaresTR(2)))
    print(str(sumSquaresTR(3)))
    print(str(sumSquaresTR(4)))
    print(str(sumSquaresTR(5)))
    print(str(sumSquaresTR(6)))

def sumSquaresAccum(n , a):
    """tail recursive function of sumSquares"""
    if n == 0:
        return a
    else:
        return sumSquaresAccum(n-1 , a + n**2)



def sumSquaresTR(n):
    """sumSquaresTR is the wrapper function for sumSquaresAccum"""
    return sumSquaresAccum(n , 0)


def stairclimb(n):
    """stairclimb expresses the number of possible ways to climb n amount of stairs"""
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 3
    else:
        return stairclimb(n-1)+ stairclimb(n-2) + stairclimb(n-3)

def stairclimbAccum(n,a,b,):
    """stairclimbAccum is the tail recursive function of stairclimb"""
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 3
    else:
        return stairclimbAccum(n-1, b, b+a)


def stairclimbTR(n):
    """stairclimbTR is the wrapper function for stairclimbTR"""
    return stairclimbAccum(n,0,1)

def stairclimbTEST():
    print(str(stairclimb(0)))
    print(str(stairclimb(1)))
    print(str(stairclimb(2)))
    print(str(stairclimb(3)))
    print(str(stairclimb(4)))
    print(str(stairclimb(5)))
    print(str(stairclimb(6)))
    print(str(stairclimbTR(0)))
    print(str(stairclimbTR(1)))
    print(str(stairclimbTR(2)))
    print(str(stairclimbTR(3)))
    print(str(stairclimbTR(4)))
    print(str(stairclimbTR(5)))
    print(str(stairclimbTR(6)))


sumSquaresTest()
stairclimbTEST()
print ("Close window when done")