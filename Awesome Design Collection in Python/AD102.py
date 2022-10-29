#awesome design 102
from turtle import *
import colorsys
bgcolor("black")
h = 0.3
speed(0)
pensize(4)

def design(ang,len):
    seth(ang)
    fd(300-len)
    seth(ang+60)
    circle(110-((110/300)*len),90)
    seth(ang-150)
    fd(300-len)
    
    
for i in range(12):
    c = colorsys.hsv_to_rgb(h,0.8,1)
    pencolor(c)
    for j in range(30):
        if j ==29:
            fillcolor(c)
            begin_fill()
            design(i*30,j*5)
            end_fill()
        else:
            design(i*30,j*5)
    h += 0.15
    
ht()
done()
