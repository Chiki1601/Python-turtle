#samsung gallery icon in python
from turtle import *
speed(6)
width(1)
pu()
goto(-125,-215)
pd()
color("#AA0144")
begin_fill()
rt(15)
for i in range(4):
    circle(400,30)
    circle(150,60)
end_fill()
pu()
goto(0,30)
pd()
lt(90)
color("white")
begin_fill()
for i in range(6):
    fd(70)
    lt(15)
    circle(40,180)
    lt(15)
    fd(70)
    rt(150)
end_fill()
pu()
goto(8,-10)
pd()
lt(15)
color("#AA0144")
begin_fill()
circle(30)
end_fill()

ht()
done()