#awesome design 138 in Pytohn
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
        fd(71)
        circle(i,10.3)
        for k in range(i):
            fd(10)
            rt(50)
            bk(9)
            circle(k,5)
            rt(90)         
            
H()
for p in range(11):
    H()
ht()
done()