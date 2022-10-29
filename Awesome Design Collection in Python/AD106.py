#awesome design 106
from turtle import *
import colorsys
bgcolor("black")
h = 0.3
speed(0)
pensize(3)

def design(ang,n):
    rt(ang)
    fd(n)
    lt(ang-30)
    bk(n)
seth(60)    
for i in range(200):
    c = colorsys.hsv_to_rgb(h,0.8,1)
    pencolor(c)
    design(60,i)
    design(30,i)
    design(60,i)
    h += 0.006
ht()
done()
