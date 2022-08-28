#flag of Bahamas
from turtle import *

speed(0)
setup(800, 500)
bgcolor("deepskyblue")

penup()
goto(-400, -80)
pendown()

# Yellow Strip
color("gold")
begin_fill()
forward(800)
left(90)
forward(167)
left(90)
forward(800)
end_fill()

# Black Triangle
left(90)
penup()
goto(-400, 250)
pendown()
color("black")
begin_fill()
forward(500)
left(130)
forward(400)
end_fill()

hideturtle()
done()
