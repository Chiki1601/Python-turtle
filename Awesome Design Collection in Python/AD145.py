#awesome design 145 in Pytohn
from turtle import *
import colorsys
tracer(968)
bgcolor("black")

def H():
    h = 0
    n = 20
    up()
    goto(0,60)
    down()
    pensize(5)
    for i in range(449):
        c = colorsys.hsv_to_rgb(h,1,1)
        color(c)
        h +=1/n
        fd(10)
        circle(i,4.5)
        for j in range(550):
            lt(971)
            circle(i*1,j,steps=2)
            circle(i,2)
            
            
H()
ht()
done()
