#flag of Pakistan

from turtle import *
setup(1020,700)
speed(5)
pu()
goto(-500,275)
pd()
color("black","dark green")
begin_fill()
for n in range(2):
    fd(1000)
    rt(90)
    fd(550)
    rt(90)
    
end_fill()
pu()
goto(150,0)
pd()
pu()
backward(75)
lt(90)
fd(125)
lt(90)

color("white")
pd()

begin_fill()
circle(127.5)
end_fill()
pu()
goto(113,127.5)
color("dark green")
pd()
begin_fill()
circle(107)
end_fill()
pu()
goto(225,20)
color("white")
pd()
rt(20)
begin_fill()
for x in range(5):
    fd(100)
    rt(144)
end_fill()
pu()
goto(-250,-275)
color("black","white")
lt(20)
pd()
begin_fill()
for n in range(1):
    fd(250)
    rt(90)
    fd(550)
    rt(90)
    fd(250)
end_fill()
pu()
color("black")
write("Flag of Pakistan",font=("Arial",25,"normal"))
pu()
goto(0,800)
pd()
done()