#awesome design 111
from turtle import *
import colorsys
bgcolor("black")
h = 0
n = 100
speed(0)
pensize(3)
for i in range(90):
    c = colorsys.hsv_to_rgb(h,1,0.8)
    pencolor(c)
    h += 1 /n
    lt(250)
    fd(i*2)
    rt(40)
    bk(i*3)
    circle(60,90)

ht()
done()
