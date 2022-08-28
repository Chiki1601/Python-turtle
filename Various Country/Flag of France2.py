#flag of France2
from turtle import *

speed(0)
setup(800, 500)

penup()
goto(-400, 250)
pendown()

# Blue Rectangle
color("darkblue")
begin_fill()
forward(267)
right(90)
forward(500)
right(90)
forward(267)
end_fill()

right(180)
penup()
forward(534)
pendown()

# Red Rectangle
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
