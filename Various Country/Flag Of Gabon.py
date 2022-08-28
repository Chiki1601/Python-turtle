#flag of Gabon
from turtle import *

speed(0)
setup(800, 500)

penup()
goto(-400, 250)
pendown()

color("#00b33f")
begin_fill()
forward(800)
right(90)
forward(167)
right(90)
forward(800)
end_fill()

left(90)

color("#ffc400")
begin_fill()
forward(167)
left(90)
forward(800)
left(90)
forward(167)
end_fill()

left(180)
penup()
forward(167)
pendown()

color("#0066ff")
begin_fill()
forward(167)
right(90)
forward(800)
right(90)
forward(167)
end_fill()

hideturtle()
done()
