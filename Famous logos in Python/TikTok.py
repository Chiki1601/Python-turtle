#tic tok logo in Python

from turtle import *

speed(3)
pos = [(0,0),(-5,13),(-5,5)]
pensize(30)
bgcolor("black")
colors=['red','turquoise','white']

for(x,y),\
 i in zip(pos,colors):
    penup()
    goto(x,y)
    pendown()
    color(i)
    left(180)
    circle(50,270)
    forward(120)
    left(180)
    circle(50,90)
    
penup()
goto(-150,-230)
pendown()
hideturtle()
done()
