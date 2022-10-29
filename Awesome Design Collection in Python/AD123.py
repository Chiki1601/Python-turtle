#awesome design 123 in Pytohn
from turtle import *
import colorsys
bgcolor("black")
h = 0.8
speed(0)
for i in range(180):
    c = colorsys.hsv_to_rgb(h,1,1)
    fillcolor(c)
    h += 0.004
    begin_fill()
    circle(190-i,90)
    lt(20)
    lt(90)
    circle(190-i,90)
    rt(80)
    end_fill()
ht()
done()
