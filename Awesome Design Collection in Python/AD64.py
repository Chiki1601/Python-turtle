#Awesome Design 64
from turtle import *
speed(50)
def p(x,y):
    pu()
    goto(x,y)
    pd()
    
color= ["red","yellow","blue","green"]
a = 1
for x in range(4000):
    p(0,0)
    fillcolor(color[x%4])
    begin_fill()
    circle(100-a,60)
    p(0,0)
    circle(-100+a,60)
    lt(6)
    end_fill()
    a +=1
    
done()
