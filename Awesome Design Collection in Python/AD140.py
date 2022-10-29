#awesome design 140 in Pytohn
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
    for i in range(100):
        c = colorsys.hsv_to_rgb(h,1,1)
        color(c)
        h +=1/n
        fd(101)
        circle(i,5)
        for k in range(i):
            fd(12)
            rt(35)
            bk(5)
            circle(k,10)
            rt(5)         
            
H()
for p in range(11):
    H()
ht()
done()
