#awesome Design 59 in Python
from turtle import *
import random
speed(10)
bgcolor("black")
color= ["red","yellow","blue","green"]
ht()

def p(x,y):
    pu()
    goto(x,y)
    pd()
def Pooja():
    for x in range(100):
        x=random.randint(-900,200)
        y=random.randint(-1000,1000)
        p(x,y)
        pencolor(color[x%4])
        pensize(10)
        for y in range(4):
            fd(200)
            lt(90)
Pooja()
done()
        
