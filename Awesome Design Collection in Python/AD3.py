#Awesome design 3 in Python turtle
import colorsys as cs
from turtle import *

speed(0)
bgcolor('black')
pensize(2)
hideturtle()

hue = 0.0

for i in range(18):
    for x in range(28):
        colors = cs.hsv_to_rgb(hue,1,1)
        color(colors)
        hue +=0.005
        rt(90)
        circle(170-x*6,90)
        lt(90)
        circle(170-x*6,90)
        rt(180)
    circle(50,20)
done()
