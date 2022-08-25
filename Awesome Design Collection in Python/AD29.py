#Awesome design 29

from turtle import *


speed(0)
pensize(4)
penup()
pencolor('limegreen')
bgcolor('black')
setup(800,800)
goto(10,0)
pendown()

for i in range(40):
    right(90)
    forward(i*5)

    for i in range(8):
        forward(150)
        right(90)

hideturtle()
exitonclick()
