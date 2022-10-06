#awesome design 122
from turtle import *
import colorsys
bgcolor("black")
h = 0.2
speed(0)
for i in range(170):
    c = colorsys.hsv_to_rgb(h,1,1)
    fillcolor(c)
    h += 0.02
    begin_fill()
    circle(190-i,90)
    lt(90)
    circle(190-i,90)
    lt(10)
    end_fill()
    
ht()
done()
