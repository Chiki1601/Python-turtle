#pink ice cream cone drawing in Python

import turtle
import random

t = turtle.Turtle()
screen = turtle.Screen()
t.speed(0)


screen.bgcolor("light blue")


t.penup()
t.goto(-150,0)
t.pendown()
t.begin_fill()

for i in range(3):
    t.forward(350)
    t.right(120)
    
t.end_fill()

t.begin_fill()
t.right(45)
t.color('pink')


for i in range(4):
    for i in range(10):
        t.forward(10)
        t.left(10)
    t.right(100)
    
t.end_fill()
    
    
t.left(100)
left =15
t.begin_fill()

for i in range(41):        
        t.left(6)
        t.forward(21.7)
        left +=1
       
        
t.end_fill()
turtle.done()
