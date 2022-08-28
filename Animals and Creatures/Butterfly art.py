#butterfly art

from turtle import *
from math import sin,cos,e
def draw():
    cycle=25
    t=0
    a=b=40
    while not (t>cycle*360):
        p=e**cos(t)-2*cos(4*t)+sin(t/12)**5
        x=a*sin(t)*p
        y=b*cos(t)*p
        goto(x,y)
        dot()
        t+=1
        print(t)
        pencolor("red")
        pu()
        speed(0)
        tracer(1000)
        
draw()
ht()
done()
