#awesome design 108
from turtle import *
import colorsys
bgcolor("black")
h = 0.99
speed(0)
pensize(3)

def design(ang,n):
    circle(90+n,90)
    lt(ang)
    circle(90+n,90)
pu()
goto(-70,0)
pd()
    
for i in range(160):
    c = colorsys.hsv_to_rgb(h,0.8,1)
    pencolor(c)
    design(180,i)
    pu()
    design(45,i)
    pd()
    design(180,i)
    pu()
    design(45,i)
    pd()
    h += 0.005

ht()
done()
