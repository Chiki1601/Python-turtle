#awesome design 92 in Python
#awesome design 92
from turtle import *
import colorsys
bgcolor("black")
h = 0.25
speed(0)
pensize(3)
def design(ang,n):
    circle(30+n,90)
    lt(ang)
    circle(90+n,60)
pu()
goto(0,70)
pd()
seth(15)
for i in range(80):
    c = colorsys.hsv_to_rgb(h,0.8,1)
    pencolor(c)
    design(180,i)
    design(80,i)
    design(20,i)
    design(80,i)
    h += 1/90
    
ht()
done()
