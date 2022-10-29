#awesome design 89
from turtle import *
import colorsys
bgcolor("black")
h = 0.0
tracer(10)
speed(10)
pensize(10)
for i in range(500):
    col = colorsys.hsv_to_rgb(h,1,1)
    color(col)
    up()
    goto(0,0)
    fd(i)
    down()
    circle(i,-45)
    lt(40)
    h += 0.005
ht()
done()
