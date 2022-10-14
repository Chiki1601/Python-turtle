#awesome design 128 in Python
from turtle import *
import colorsys
tracer(232)
bgcolor("black")

def H():
    h = 0
    n =8

    for i in range(428):
        c = colorsys.hsv_to_rgb(h,1,1)
        color('black')
        up()
        goto(0,0)
        down()
        h +=1/n
        pensize(1)
        rt(123)
        circle(i,4)
        lt(10)
        fd(i*3)
        for j in range(i):
            color(c)
            fillcolor("black")
            begin_fill()
            rt(94)
            circle(j,397,steps=1)
            end_fill()
        
H()        
ht()
done()
