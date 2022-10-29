#awesome design 119
from turtle import *
import colorsys
bgcolor("black")
h = 0.99
speed(0)
def design(ang,n):
    circle(30+n,60)
    lt(ang)
    circle(30+n,60)
    
for i in range(130):
    c = colorsys.hsv_to_rgb(h,0.8,1)
    pencolor(c)
    
    pu()
    design(150,i)
    design(60,i)
    pd()
    design(150,i)
    design(60,i)
    design(30,i)
    pd()
    design(151,i)
    pu()
    h += 0.003
ht()
done()
