#awesome design 114 in Python
from turtle import *
bgcolor("black")
h = 0
n=200
speed(0)
pensize(3)
colors=("red","green","blue","yellow","cyan","purple","seagreen","orange","black","white")
for col in colors:
    pencolor(col)
    begin_fill()
    for i in range(8):
        lt(144)
        for j in range(2):
            fd(n)
            lt(60)
            fd(n)
            lt(120)
    n = n-20
    end_fill()    
ht()
done()
