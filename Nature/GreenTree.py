#Green tree in Python
from turtle import *
from math import *
from random import *

def tree(n,k):
    pd()
    
    
    t = cos(radians(heading()+45))/4+0.25
    pensize(n*3)
    pencolor("black")
    forward(k)
    if n>0:
        b = random()*15+14
        c = random()*15+12
        d = k*(random()*0.25+0.7)
        
        right(b)
        tree(n-1,d)
        left(b+c)
        tree(n-1,d)
        right(c)
        
    else:
        right(90)
        n = cos(radians(heading()-45))/4+0.5
        color("green","green")
        begin_fill()
        circle(12)
        lt(90)
        fillcolor("green")
        end_fill()
    pu()
    backward(k)
    
bgcolor(0.5,0.5,0.5)
ht()
speed(5)
tracer(0,0)
pu()
backward(100)
lt(90)
pu()
backward(300)
tree(10,103)
done()
