#samsung camera logo in Python

from turtle import *
speed(3)
width(1)
pu()
goto(-105,-205)
pd()
color("#F2003C")
begin_fill()
rt(15)
for i in range(4):
    circle(400,30)
    circle(150,60)
end_fill()
pu()

goto(-104,-90)
pd()
color("white")
begin_fill()
lt(15)
for i in range(2):
    fd(210)
    circle(25,90)
    fd(130)
    circle(25,90)
end_fill()
goto(0,-45)
color("#AA0144")
begin_fill()
circle(45)
end_fill()
pu()

goto(80,20)
pd()

color("#F2003C")
begin_fill()
circle(25)
end_fill()
ht()
done()
