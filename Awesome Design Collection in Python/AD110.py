#awesome design 110
from turtle import *
import colorsys
bgcolor("black")
h = 0.99
speed(0)
pensize(3)


def design(ang,n):
    circle(60+n,90)
    lt(ang)
    circle(60+n,90)
pu()
goto(-30,0)
pd()
for i in range(160):
    c = colorsys.hsv_to_rgb(h,0.8,1)
    pencolor(c)
    design(151,i)
    design(59,i)
    design(151,i)
    design(59,i)
    
    h += 0.011

ht()
done()
