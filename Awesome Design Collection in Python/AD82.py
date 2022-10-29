#awesome design 82 in python

from turtle import *
import colorsys
speed(0)
bgcolor("black")
h = 0.3
def design(ang,n):
    circle(70+n,90)
    left(ang)
    circle(70+n,90)
for i in range(100):
    col = colorsys.hsv_to_rgb(h,0.8,1)
    h += 0.007
    color(col)
    design(60,i)
    design(90,i)
    design(60,i)
    design(90,i)
    design(60,i)
ht()
done()
