#awesome design 107
from turtle import *
import colorsys
bgcolor("black")
h = 0.3
speed(0)
pensize(3)

def design(ang,n):
    circle(20+n,90)
    lt(ang)
    circle(20+n,90)
    
for i in range(120):
    c = colorsys.hsv_to_rgb(h,0.8,1)
    pencolor(c)
    design(151,i)
    pu()
    design(59,i)
    pd()
    design(151,i)
    h += 1/80
ht()
done()
