#awesome design 97
from turtle import *
import colorsys
bgcolor("black")
h = 1
speed(0)
pensize(3)
def design(ang,n):
    circle(50+n,90)
    lt(ang)
    circle(50+n,90)
pu()
goto(0,60)
pd()
for i in range(120):
    c = colorsys.hsv_to_rgb(h,0.8,1)
    pencolor(c)
    pu()
    design(91,i)
    design(180,i)
    pd()
    design(180,i)
    pu()
    design(91,i)
    pd()
    
    if i<=15:
        h = 1
    else:
        h += 0.005
ht()
done()
