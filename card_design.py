"""file: card_design.py
CSCI-141 Lab
author: Chase Lewis
created: August 2017"""

import turtle


def initialization():
    """this function intializes the turle"""
    turtle.up()
    turtle.left(180)
    turtle.forward(200)
    turtle.down()
    turtle.right(180)
    turtle.speed(0)

   
def draw_card_border():
    """this function draws the border of the of the card""" 
    turtle.down()
    turtle.forward(125)
    turtle.left(90)
    turtle.forward(200)
    turtle.left(90)
    turtle.forward(125)
    turtle.left(90)
    turtle.forward(200)
    turtle.left(90)

def draw_card_suit_diamond():
    """draw_card_suit will draw the suit(diamond) on the border"""
    turtle.pencolor("red")
    turtle.fillcolor("red")
    turtle.begin_fill()
    turtle.right(45)
    turtle.forward(15)
    turtle.right(90)
    turtle.forward(15)
    turtle.right(90)
    turtle.forward(15)
    turtle.right(90)
    turtle.forward(15)
    turtle.end_fill()
    turtle.pencolor("black")

def draw_card_big_suit_diamond():
    """draw_card_big_suit will draw the bigger suit(diamond) in the center of the card"""
    turtle.pencolor("red")
    turtle.fillcolor("red")
    turtle.begin_fill()
    turtle.right(45)
    turtle.forward(30)
    turtle.right(90)
    turtle.forward(30)
    turtle.right(90)
    turtle.forward(30)
    turtle.right(90)
    turtle.forward(30)
    turtle.end_fill()
    turtle.pencolor("black")

def draw_card_suit_club():
    turtle.fillcolor("black")
    turtle.begin_fill()
    turtle.left(90)
    turtle.circle(5)
    turtle.right(180)
    turtle.circle(5)
    turtle.up()
    turtle.left(180)
    turtle.forward(3)
    turtle.right(90)
    turtle.down()
    turtle.circle(5)
    turtle.up()
    turtle.right(90)
    turtle.forward(5)
    turtle.left(90)
    turtle.down()
    turtle.forward(2.5)
    turtle.right(90)
    turtle.forward(5)
    turtle.right(90)
    turtle.forward(5)
    turtle.right(90)
    turtle.forward(2)
    turtle.right(90)
    turtle.forward(2.5)
    turtle.left(90)
    turtle.up()
    turtle.forward(5)
    turtle.right(90)
    turtle.end_fill()

def draw_card_bigger_suit_club():
    turtle.fillcolor("black")
    turtle.begin_fill()
    turtle.left(90)
    turtle.circle(15)
    turtle.end_fill()
    turtle.right(180)
    turtle.fillcolor("black")
    turtle.begin_fill()
    turtle.circle(15)
    turtle.end_fill()
    turtle.up()
    turtle.left(180)
    turtle.forward(12)
    turtle.right(90)
    turtle.down()
    turtle.fillcolor("black")
    turtle.begin_fill()
    turtle.circle(15)
    turtle.end_fill()
    turtle.up()
    turtle.right(90)
    turtle.forward(15)
    turtle.left(90)
    turtle.down()
    turtle.fillcolor("black")
    turtle.begin_fill()
    turtle.forward(7.5)
    turtle.right(90)
    turtle.forward(15)
    turtle.right(90)
    turtle.forward(15)
    turtle.right(90)
    turtle.forward(15)
    turtle.right(90)
    turtle.forward(7.5)
    turtle.left(90)
    turtle.up()
    turtle.forward(12)
    turtle.right(90)
    turtle.end_fill()
    
    

    

def card_suit_position():
    """card_suit_position sets up the suits position"""
    turtle.up()
    turtle.forward(110)
    turtle.left(90)
    turtle.forward(25)
    turtle.right(90)
    turtle.down()
    draw_card_suit_diamond()
    turtle.up()
    turtle.right(45)
    turtle.forward(15)
    turtle.left(90)
    turtle.forward(175)
    turtle.left(90)
    turtle.forward(110)
    turtle.left(90)
    turtle.forward(8)
    turtle.left(90)
    draw_card_suit_diamond()
    turtle.up()
    turtle.left(45)
    turtle.forward(8)
    turtle.left(90)
    turtle.forward(15)
    turtle.left(90)
    turtle.forward(105)
    turtle.left(90)
    turtle.forward(62.5)
    turtle.left(90)
    turtle.forward(15)
    turtle.right(90)
    turtle.down()
    draw_card_big_suit_diamond()
    turtle.up()
    turtle.left(45)
    turtle.write( "A", align="center", font=("Arial", 20, "bold"))
    turtle.home()

def card_suit_position_two():
    """card_suit_position_two sets up the suit of the second card on right"""
    turtle.forward(30)
    draw_card_border()
    turtle.up()
    turtle.forward(110)
    turtle.left(90)
    turtle.forward(25)
    turtle.right(90)
    turtle.down()
    draw_card_suit_club()
    turtle.up()
    turtle.forward(15)
    turtle.left(90)
    turtle.forward(175)
    turtle.left(90)
    turtle.forward(110)
    turtle.left(90)
    turtle.forward(20)
    turtle.left(90)
    turtle.down()
    draw_card_suit_club() 
    turtle.up()
    turtle.left(90)
    turtle.forward(20)
    turtle.left(90)
    turtle.forward(15)
    turtle.left(90)
    turtle.forward(125)
    turtle.left(90)
    turtle.forward(62.5)
    turtle.left(90)
    turtle.forward(15)
    turtle.right(90)
    turtle.down()
    draw_card_bigger_suit_club()
    turtle.up()
    turtle.left(90)
    turtle.forward(30)
    turtle.down()
    turtle.write( "7", align="center", font=("Arial", 20, "bold"))
    
    
    


def main():
    """main runs all of the functions"""
    initialization()
    draw_card_border()
    card_suit_position()
    card_suit_position_two()
    print ("Close window you are finished")
    turtle.done()
    
    
    
    
    
    
   
    

main()
    

     
