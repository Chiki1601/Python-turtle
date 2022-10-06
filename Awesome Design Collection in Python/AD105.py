#awesome design 105
from turtle import *
import colorsys
bgcolor("black")
h = 0.3
speed(0)
pensize(4)
for i in range(550):
    c = colorsys.hsv_to_rgb(h,1,1)
    pencolor(c)
    h += 0.004
    circle(190-i,30)
    rt(20)
    lt(220)
    circle(190-i,30)
    
ht()
done()
