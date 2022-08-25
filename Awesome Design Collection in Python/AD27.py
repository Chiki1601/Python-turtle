#awesome design 27
from turtle import *
speed(0)
bgcolor('black')
pencolor('steelblue')

for i in range(120):
    right(i)
    circle(200,i)
    forward(i)
    right(90)
    forward(i)

hideturtle()
done()
