#awesome design 104
from turtle import *
import colorsys
bgcolor("black")
h = 0.3
speed(0)
pensize(30)

def design(ang,r):
    seth(ang)
    circle(200-r,130)
    seth(ang+180)
    circle(200-r,130)
    
    
for i in range(20):
    c = colorsys.hsv_to_rgb(h,0.89,1)
    pencolor(c)
    for j in range(15):
        design(i*20,j*10)
    h += 0.1
    
ht()
done()
