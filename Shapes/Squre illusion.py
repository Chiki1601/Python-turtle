#square illusion in Python

from turtle import *
import random
speed(8)
setup(700,700)
def Square(x,y,size,tilt_angle,c):
    up()
    goto(x,y)
    down()
    seth(tilt_angle)
    fillcolor(c)
    begin_fill()
    for i in range(4):
        fd(size)
        rt(90)   
    end_fill()
angle = 0
size = 300

while size>0:
    Square(0,0,size,angle,(random.uniform(0,1),random.uniform(0,1),random.uniform(0,1)))
    size-=0.1
    angle+=3

ht()
done()
