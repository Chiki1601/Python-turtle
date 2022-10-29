#awesome design 130 in Python
from turtle import *
import colorsys
tracer(232)
bgcolor("black")

def H():
    h = 0
    n =8

    for i in range(500):
        c = colorsys.hsv_to_rgb(h,1,1)
        color('black')
        up()
        goto(0,0)
        down()
        h +=1/n
        pensize(1)
        rt(150)
        circle(i,5)
        lt(10)
        fd(i*3)
        for j in range(i):
            color(c)
            fillcolor("black")
            begin_fill()
            rt(50)
            circle(j,425,steps=50)
            end_fill()
        
H()        
ht()
done()
