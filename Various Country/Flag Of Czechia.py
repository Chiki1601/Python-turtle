#flag of Czechia
from turtle import *

speed(0)
setup(800, 500)

penup()
goto(-400, -250)
pendown()

# Red rectangle
color("firebrick")
begin_fill()
forward(800)
left(90)
forward(250)
left(90)
forward(800)
end_fill()

left(90)

# Triangle
penup()
goto(-400, 250)
pendown()
color("navy")
begin_fill()
forward(500)
left(130)
forward(390)
end_fill()

hideturtle()
done()
