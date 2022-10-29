#awesome design 117 in Pytohn
from turtle import *
import colorsys
bgcolor("black")
h = 0
speed(0)
width(3)
pencolor("grey")
for i in range(180):
    c = colorsys.hsv_to_rgb(h,0.8,1)
    pencolor(c)
    fd(250)
    rt(-35)
    circle(80,130)
    rt(10)
    fd(100)
    pu()
    speed(0)
    bk(100)
    rt(-10)
    circle(80,-130)
    rt(35)
    bk(250)
    rt(2)
    pd()
    h += 0.011
    
ht()
done()
