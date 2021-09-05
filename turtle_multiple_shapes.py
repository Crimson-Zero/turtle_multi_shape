# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 15:41:59 2021

@author: wajee
"""


import importlib
import turtle
from turtle import Turtle , Screen
importlib.reload(turtle)

def draw_triangle(timmy):
    
     timmy.color("blue")
     
     for triangle_length in range(3):
        timmy.forward(100)
        timmy.right(120)

def draw_square(timmy):
    
     for square_length in range(4):
        timmy.forward(100)
        timmy.color("green")
        timmy.right(90)
    
def draw_pentagon(timmy):
   
    for pent in range(5):
        
        timmy.forward(100)
        timmy.color("black")
        timmy.right(72)
            
def draw_hexagon(timmy):
    
    for hexa in range(6):
        
        timmy.forward(100)
        timmy.color("red")
        timmy.right(60)
        
def draw_heptagon(timmy):
    
    for hepta in range(7):
        
        timmy.forward(100)
        timmy.color("brown")
        timmy.right(51.43)

def draw_octagon(timmy):
    
    for oct in range(8):
        
        timmy.forward(100)
        timmy.color("pink")
        timmy.right(45)

def draw_nonagon(timmy):
    
    for non in range(9):
        
        timmy.forward(100)
        timmy.color("pink")
        timmy.right(40)

def draw_decagon(timmy):
    
    for non in range(10):
        
        timmy.forward(100)
        timmy.color("orange")
        timmy.right(36)


def main():
    
    
    timmy=Turtle()
    timmy.shape("turtle")
    screen=Screen()
    draw_triangle(timmy)
    draw_square(timmy)
    draw_pentagon(timmy)
    draw_hexagon(timmy)
    draw_heptagon(timmy)
    draw_octagon(timmy)
    draw_nonagon(timmy)
    draw_decagon(timmy)
    
    screen.exitonclick()


if __name__=='__main__':
    main()