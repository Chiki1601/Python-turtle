#flag of Mauritania
from turtle import *

setup(800, 500)
speed(0)
bgcolor("seagreen")

# Moon Shape
penup()
goto(0, -135)
pendown()
color("gold")
begin_fill()
circle(250)
end_fill()

penup()
goto(0, -65)
pendown()
color("seagreen")
begin_fill()
circle(300)
end_fill()

# Star
penup()
goto(-65, 75)
pendown()
color("gold")
begin_fill()
for i in range(5):
    forward(120)
    right(144)
end_fill()

# Top Rectangle
penup()
goto(-400, 250)
pendown()
color("firebrick")
begin_fill()
for i in range(2):
    forward(800)
    right(90)
    forward(75)
    right(90)
end_fill()

# Bottom Rectangle
penup()
goto(-400, -250)
pendown()
begin_fill()
for i in range(2):
    forward(800)
    left(90)
    forward(75)
    left(90)
end_fill()

hideturtle()
done()
