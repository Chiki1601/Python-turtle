#VI logo in Python

from turtle import *
bgcolor("red")

pu()
goto(-40,50)
pd()

color("white")
begin_fill()
for i in range(2):
    fd(-30)
    rt(-120)
    fd(-100)
    rt(-60)
end_fill()
pu()
goto(60,50)
pd()
color("white")
begin_fill()
for i in range(2):
    fd(30)
    rt(120)
    fd(100)
    rt(60)
end_fill()


pu()
goto(100,50)
pd()
color("white")
begin_fill()
for i in range(2):
    fd(30)
    rt(90)
    fd(90)
    rt(90)
end_fill()

pu()
goto(115,-60)
pd()
color("orange")
begin_fill()
dot(30)
end_fill()
    
ht()
done()
