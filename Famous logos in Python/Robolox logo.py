#robolox logo in Python

from turtle import *
width(1)
speed(3)
pu()
goto(-100,-100)
pd()
begin_fill()
for i in range(4):
    fd(200)
    circle(50,90)
end_fill()
goto(80,-70)
color("white")
begin_fill()
lt(80)
for i in range(4):
    fd(200)
    lt(90)
end_fill()
goto(15,20)
color("black")
begin_fill()
for i in range(4):
    fd(40)
    lt(90)
end_fill()
ht()
done()
