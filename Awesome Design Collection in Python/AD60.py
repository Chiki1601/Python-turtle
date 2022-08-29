#Awesome Design 60

from turtle import *
import random

bgcolor("black")
color= ["red","yellow","blue","green","purple","white","orange"]
ht()
def p(x,y):
    pu()
    goto(x,y)
    pd()
def hexa():
    for x in range(3):
        fd(a)
        lt(120)
        
def hexa2():
    for x in range(3):
        fd(a)
        rt(120)
        
for x in range(0,120):
    fillcolor(color[x%7])
    begin_fill()
    speed(500)
    
    a=random.randint(0,120)
    m=random.randint(-999,999)
    n=random.randint(-999,999)
    pencolor(color[x%7])
    p(m,n)
    hexa()
    hexa2()
    end_fill()
    speed(500)
done()
