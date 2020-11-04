""" raindrops.py
author:Chase Lewis
created:September 2017
CSci-141"""

import turtle as t

import random

import math


radius = random.randint

def init():
    """ initializes the the program"""
    t.up()
    t.right(90)
    t.fd(100)
    t.left(90)
    t.left(180)
    t.forward(300)
    t.left(90)
    t.forward(200)
    t.left(90)

def draw_pond(x,y):
    """draw_pond draws the bond pond for the rain drops"""
    t.fillcolor("light blue")
    t.begin_fill()
    t.down()
    t.forward(x)
    t.left(90)
    t.forward(y)
    t.left(90)
    t.forward(x)
    t.left(90)
    t.forward(y)
    t.end_fill()
    t.left(90)
    t.up()
    t.forward(x / 2)
    t.left(90)
    t.forward(y / 2)

def draw_raindrop0():
    """draw_raindrop0 asks the user for input"""
    x = int(input("How many raindrops? (1-100)"))
    if x > MAX_RAINDROPS():
        if x < MIN_RAINDROPS():
            print("Raindrops must be between 1 and 100 inclusive")
    else:
        print(nonRain(x))


def draw_raindrop1():
    """draw_raindrop1 draws the rain drops"""
    t.setpos(random.randint(-250,250), random.randint(-250,250))
    t.fillcolor(random.random(), random.random(), random.random())
    t.begin_fill()
    t.circle(radius)
    t.end_fill()
    return 2*math.pi*radius + draw_ripples(radius, 5, 0)

def nonRain():
    """nonRain adds the circumferences up together"""
    if x == 0:
        circumference = 0
        return circumference
    else:
        return draw_raindrop1() + nonRain(x - 1)

    
def draw_ripples(radius,n,c):
    """"draw_ripples draws the tail recursive ripples"""
    if n == 0:
        return c
    else:
        t.up()
        t.right(90)
        t.forward(radius)
        t.left(90)
        t.down()
        t.circle(radius*n)
        return draw_ripples(radius, n - 1, c + 2*math.pi*n)

def MAX_RAINDROPS():
    "MAX_RAINDROPS returns the max amount of raindrops"
    return 100

def MIN_RAINDROPS():
    """MIN_RAINDROPS returns the min amount of raindrops"""
    return 1

def main():
    """main runs all of the functions"""
    init()
    MAX_RAINDROPS()
    MIN_RAINDROPS()
    draw_pond(600,600)
    draw_raindrop0()
    draw_raindrop1()
    nonRain()
    draw_ripples(radius,5,0)



main()
