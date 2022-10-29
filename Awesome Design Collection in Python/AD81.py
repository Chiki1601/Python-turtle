#awesome design 81 in Python
from turtle import *
import colorsys
speed(0)
bgcolor("black")
h = 0
def design(ang,n):
    circle(60+n,90)
    left(ang)
    circle(60+n,90)
for i in range(100):
    col = colorsys.hsv_to_rgb(h,0.8,1)
    h += 0.006
    color(col)
    design(75,i)
    design(45,i)
    design(120,i)
    design(45,i)
    design(75,i)
ht()
done()
