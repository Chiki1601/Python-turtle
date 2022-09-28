#awesome design 84

from turtle import *
import colorsys
bgcolor("black")
h = 1
n = 5
speed(0)
goto(-100,50)
width(4)
for i in range(180):
    c = colorsys.hsv_to_rgb(h,1,0.9)
    h += 1/n
    lt(150)
    color(c)
    for i in range(5):
        fd(100)
        lt(55)
    
ht()
done()
