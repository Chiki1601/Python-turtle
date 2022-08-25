#awesome design 28
from turtle import *


speed(0)
pensize(3)
penup()
pencolor('indigo')
bgcolor('black')
setup(800,800)
goto(10,0)
pendown()

for i in range(40):
    right(90)
    forward(i*6)

    for i in range(8):
        forward(140)
        right(270)

hideturtle()
exitonclick()
