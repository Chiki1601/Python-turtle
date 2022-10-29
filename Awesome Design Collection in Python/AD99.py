#awesome design 99
from turtle import *
import colorsys
bgcolor("black")
h = 0.3
speed(0)
pensize(4)

def design(ang,len):
    seth(ang)
    fd((200/82)*len)
    seth(ang+135)
    fd((200/82)*len)
    seth(ang-90)
    fd(len)
    seth(ang-135)
    fd(len)
    
for i in range(8):
    c = colorsys.hsv_to_rgb(h,0.8,1)
    pencolor(c)
    for j in range(10):
        design(i*45,100-(2*j))
    h += 0.2

ht()
done()
