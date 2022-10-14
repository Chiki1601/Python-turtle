#awesome design 147 in Pytohn
from turtle import *
import colorsys
bgcolor("black")
pensize(2)
speed(0)
n = 100
h = 0
for i in range(85):
    c = colorsys.hsv_to_rgb(h,1,0.8)
    color(c)
    h +=1/n
    rt(120)
    circle(i*1.2,-180)
    circle(i,180)
    circle(i,60)
    
ht()
done()
