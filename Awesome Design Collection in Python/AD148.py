#awesome design 148 in Pytohn
from turtle import *
import colorsys
bgcolor("black")
pensize(2)
speed(0)
n = 100
h = 0
for i in range(101):
    c = colorsys.hsv_to_rgb(h,1,0.8)
    color(c)
    h +=1/n
    rt(120)
    circle(i*1.2,-180)
    circle(i,190)
    circle(i,120)
    circle(i,60)
    circle(i,30)
    circle(i,115)
    
ht()
done()
