#awesome design 113
from turtle import *
import colorsys
bgcolor("black")
h = 0.8
speed(0)
pensize(4)
def heart(ang,len=100):
    seth(ang)
    fd(len)
    circle((60/100)*len,180)
    seth(ang-130)
    fd((155/100)*len)
    seth(ang+100)
    fd(len)
    circle(-(60/100)*len,180)
    seth(ang-130)
    fd((155/100)*len)
for i in range(170):
    c = colorsys.hsv_to_rgb(h,0.8,1)
    pencolor(c)
    h += 0.01
    fillcolor(c)
    begin_fill()
    heart((i*120)-20,-i+200)
    end_fill()
ht()
done(0)
