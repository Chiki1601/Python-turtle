#awesome design 125 in Pytohn
from turtle import *
import colorsys
bgcolor("black")
h = 0.8
speed(0)
for i in range(180):
    c = colorsys.hsv_to_rgb(h,1,1)
    fillcolor(c)
    h += 0.02
    begin_fill()
    circle(120-i,90)
    lt(20)
    lt(90)
    circle(120-i,90)
    rt(60)
    end_fill()
ht()
done()
