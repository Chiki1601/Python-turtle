#awesome design 94
from turtle import *
import colorsys
bgcolor("black")
h = 0.3
speed(0)
pensize(3)
def design(ang,n):
    rt(ang)
    fd(n)
    lt(ang)
    fd(n)

for i in range(120):
    c = colorsys.hsv_to_rgb(h,0.8,1)
    pencolor(c)
    design(60,i)
    circle(i,90)
    design(60,i)
    circle(i,180)
    pd()
    design(60,i)
    h += 0.006
    
ht()
done()
