#flag of Chad
from turtle import *

speed(0)
setup(800, 500)

penup()
goto(-400, 250)
pendown()

color("darkblue")
begin_fill()
forward(267)
right(90)
forward(500)
right(90)
forward(267)
end_fill()

right(180)
forward(267)

color("yellow")
begin_fill()
left(90)
forward(500)
right(90)
forward(267)
right(90)
forward(500)
end_fill()

left(90)

color("red")
begin_fill()
forward(267)
left(90)
forward(500)
left(90)
forward(267)
end_fill()

hideturtle()
done()
