#awesome design 146 in Pytohn
from turtle import *
import colorsys
tracer(968)
bgcolor("black")

def H():
    h = 0
    n = 5
    up()
    goto(0,60)
    down()
    pensize(5)
    for i in range(50):
        c = colorsys.hsv_to_rgb(h,1,1)
        color(c)
        h +=1/n
        fd(101)
        circle(i,55)
        for j in range(50):
            lt(971)
            circle(i*10,j,steps=2)
            circle(i,2)
            
            
H()
ht()
done()
