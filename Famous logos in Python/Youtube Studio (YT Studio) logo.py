#yt studio logo in Python
from turtle import *
speed(2)
width(3)
color("red")
begin_fill()
lt(30)
fd(60)
circle(10,60)
fd(60)
circle(10,60)
fd(60)
circle(10,60)
fd(60)
circle(10,60)
fd(60)
circle(10,60)
fd(60)
circle(10,60)
end_fill()
goto(0,30)
color("white")
for i in range(6):
    fd(30)
    circle(10,60)
pu()
goto(-17,47)
pd()
begin_fill()
for i in range(3):
    fd(40)
    lt(120)
end_fill()
ht()
done()
