#Awesome Design 4 in Python
from turtle import *

import colorsys

speed(0)
hideturtle()
bgcolor('Black')
tracer(5)
width(2)
h = 0.001

for i in range(90):
    color(colorsys.hsv_to_rgb(h,1,1))
    fd(100)
    lt(60)
    fd(100)
    rt(120)
    circle(50)
    lt(240)
    fd(100)
    lt(60)
    fd(100)
    h += 0.02
    color(colorsys.hsv_to_rgb(h,1,1))
    fd(100)
    rt(60)
    fd(100)
    lt(120)
    circle(-50)
    rt(240)
    fd(100)
    rt(60)
    fd(100)
    lt(2)
    h += 0.02
done()
