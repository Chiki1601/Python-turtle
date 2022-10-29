#awesome design 80 in Python
from turtle import *
import colorsys
speed(0)
bgcolor("black")
n = 100
h = 0

for i in range(360):
    col = colorsys.hsv_to_rgb(h,1,0.8)
    h += 1/n
    color(col)
    for i in range(2):
        lt(250)
        fd(i*3)
        for k in range(3):
            lt(20)
            fd(22)
        
ht()
done()
