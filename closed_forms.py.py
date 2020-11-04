
"""file: closed_forms.py
author: Chase Lewis
created: August 2017
CSCI-141"""

import turtle


"""intializes the turtle so your turtle is on the left of the canvas """
def intialize():
    turtle.up()
    turtle.left(180)
    turtle.forward(400)
    turtle.right(180)
    turtle.down()

def draw_hexagon():
    """draw_hexagon draws a hexagon"""                
    turtle.forward(100)
    turtle.left(60)
    turtle.forward(100)
    turtle.left(60)
    turtle.forward(100)
    turtle.left(60)
    turtle.forward(100)
    turtle.left(60)
    turtle.forward(100)
    turtle.left(60)
    turtle.forward(100)
    turtle.left(60)


def draw_square():
    """draw_square draws a square"""
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)

def draw_triangle():
    """draw_triangle draws a triangle"""
    turtle.forward(100)
    turtle.left(120)
    turtle.forward(100)
    turtle.left(120)
    turtle.forward(100)
    turtle.left(120)


def shapes():
    """shapes reuses all the shapes"""
    turtle.up()
    turtle.forward(500)
    turtle.down()
    draw_hexagon()
    draw_square()
    draw_triangle()

def shapes2():
    """shapes2 draws the same shapes in a different location"""
    turtle.up()
    turtle.backward(100)
    turtle.left(270)
    turtle.forward(100)
    turtle.left(90)
    turtle.backward(700)
    shapes()
    
    


    

def main():
    """main runs all the functions"""
    intialize()
    draw_hexagon()
    draw_square()
    draw_triangle()
    shapes()
    shapes2()
    print ("Close the window")
    turtle.done()
    
    
    



    


main()
