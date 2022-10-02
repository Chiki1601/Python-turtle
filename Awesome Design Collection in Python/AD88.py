#awesome design 88
from turtle import *
import colorsys
bgcolor("black")
h = 0.2
tracer(500)
speed(0)
width(3)
up()
goto(0,0)
down()
for i in range(700):
    col = colorsys.hsv_to_rgb(h,1,1)
    color(col)
    circle(i,-91)
    circle(i,90)
    h += 0.002
ht()
done()
