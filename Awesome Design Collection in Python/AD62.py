#Awesome Design 62

from turtle import *
import colorsys
speed(0)
bgcolor("black")
pensize(2)
h = 0.5

for i in range(280):
    c = colorsys.hsv_to_rgb(h,1,1)
    color(c)
    h += 0.005
    fd(i)
    rt(20)
    lt(91)
    rt(40)
    for j in range(2):
        lt(40)
        
done()
