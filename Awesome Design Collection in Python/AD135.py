#awesome design 135 in Pytohn
from turtle import *
import colorsys
tracer(100)
bgcolor("black")

def H():
    h = 0
    n =78
    up()
    goto(0,60)
    down()
    pensize(5)
    for i in range(80):
        c = colorsys.hsv_to_rgb(h,1,1)
        color(c)
        h +=1/n
        fd(33)
        circle(i,10.3)
        for k in range(i):
            fd(25)
            rt(36)
            bk(9)
            circle(k,5.11)
            rt(90.2)         
            
H()
for p in range(17):
    H()
ht()
done()
