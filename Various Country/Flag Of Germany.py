#flag of Germany
from turtle import *

speed(0)
setup(800, 500)

penup()
goto(-400, 250)
pendown()

# Black Rectangle
color("black")
begin_fill()
forward(800)
right(90)
forward(167)
right(90)
forward(800)
end_fill()

left(90)

# Red Rectangle
color("red")
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

# Yellow Rectangle
color("yellow")
begin_fill()
forward(167)
right(90)
forward(800)
right(90)
forward(167)
end_fill()

hideturtle()
done()
