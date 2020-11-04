"""inscribe_poly.py
author:Chase Lewis
created: September 2017
CSCI-141"""

import turtle as t

import math as m

import random as r



def init():
    """init initializes the turtle"""
    t.speed(8)
    t.pensize(1.8)




def draw_davinci(n, radius):
    """draw_davinci draws circles and inscribed polygons"""
    totalL = 0
    a = 360 / n
    sides = n
    t.colormode(255)
    t.pencolor(r.randint(1, 255), r.randint(1, 255), r.randint(1, 255))
    t.circle(radius)
    t.left(a / 2)
    t.colormode(255)
    t.pencolor(r.randint(1, 255), r.randint(1, 255), r.randint(1, 255))
    while n >= 3:
        a = 360 / n
        q = radius ** 2
        c = m.sqrt((2 * q) - (2 * q * m.cos(m.radians(a))))
        t.forward(c)
        t.left(a)
        sides -= 1
        if sides == 0:
            t.forward(c / 2)
            if n <= 3:
                pass
            else:
                t.colormode(255)
                t.pencolor(r.randint(1,255),r.randint(1,255),r.randint(1,255))
                t.circle(m.sqrt(q - (c / 2)**2))
            n -= 1
            radius = m.sqrt(q - (c / 2) ** 2)
            a = 360 / n
            t.left (a / 2)
            sides = n
            t.colormode(255)
            t.pencolor(r.randint(1, 255), r.randint(1, 255), r.randint(1, 255))
            totalL = totalL + c * n

    return (float(totalL))











def main():
    """main runs all of the functions"""
    init()
    print (draw_davinci(5, 75))
    t.clear()
    print (draw_davinci(8,120))
    print ("Close window when done")


main()
t.done()


