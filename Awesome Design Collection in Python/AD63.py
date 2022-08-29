#Awesome Design 63
from turtle import *
import colorsys
speed(0)
bgcolor("black")
pensize(2)
y = 1
h = 0
ht()

def Pooja():
    c = colorsys.hsv_to_rgb(h,1,1)
    pencolor(c)
    circle(y)
    lt(120)
    
for x in range(3600):
    Pooja()
    h +=0.005
    y += 1
    
    speed(50)
done()   
