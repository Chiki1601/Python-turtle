#awesome design 112
from turtle import *
import colorsys
bgcolor("black")
h = 0.1
speed(0)
pensize(2)
for i in range(170):
    c = colorsys.hsv_to_rgb(h,1,1)
    pencolor(c)
    h += 0.2
    for j in range(2):
        fd(i)
        lt(71)
        rt(120)
    rt(240)
    lt(51)
    
ht()
done()
