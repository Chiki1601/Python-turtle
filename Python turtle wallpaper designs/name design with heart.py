#name design in Python

from turtle import *
bgcolor("white")
speed(0)
width(5)
pu()
goto(-55,-40)
pd()
color("black")
fillcolor("red")
style=("Arial",30,"bold")
write("pooja",font=style)
pu()
goto(0,45)
pd()
lt(135)
color("black")
def Heart():
    fillcolor("red")
    begin_fill()
    fd(100)
    circle(-50,180)
    lt(90)
    circle(-50,180)
    fd(100)
    end_fill()

for i in range(6):
    Heart()
    pu()
    rt(40)
    circle(60,60)
    rt(50)
    pd()

ht()
done()
