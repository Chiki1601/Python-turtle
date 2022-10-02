#awesome design 91

from turtle import *
import colorsys
bgcolor("black")
speed(0)
tracer(200)
h = 0.3
for i in range(2000):
    col = colorsys.hsv_to_rgb(h,1,1)
    color(col)
    circle(i,90)
    circle(i*2,91)
    h +=0.008

ht()
done()
