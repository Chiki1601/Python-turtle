#awesome design 85
from turtle import *
import colorsys
bgcolor("black")
h = 0.001
n = 889
pensize(2)
tracer(78)
for i in range(900):
    c = colorsys.hsv_to_rgb(h,1,0.7)
    h += 1/n
    up()
    goto(-8,25)
    down()
    pencolor(c)
    fd(i)
    rt(859)
    fillcolor(c)
    begin_fill()
    circle(15,320)
    end_fill()
    lt(179)
    bk(i)
    fd(i)
    rt(6)
    
ht()
done()
