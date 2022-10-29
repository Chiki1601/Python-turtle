#awesome design 78 in Python
from turtle import *
import colorsys
bgcolor("black")
h = 0
speed(99)

for i in range(300):
    col = colorsys.hsv_to_rgb(h,1,1)
    pencolor(col)
    h +=0.008
    fd(i)
    circle(50,i)
    rt(i)
    lt(91)
    circle(2)
    circle(30)
    circle(25)
        
ht()
done()
