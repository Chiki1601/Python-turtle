#awesome design 77 in Python
from turtle import *
import colorsys
bgcolor("black")
h = 0
speed(99)

for i in range(250):
    col = colorsys.hsv_to_rgb(h,1,1)
    pencolor(col)
    h +=0.005
    for j in range(2):
        fd(i)
        rt(60)
        fd(300)
        rt(120)
        rt(20*1)
        
ht()
done()
