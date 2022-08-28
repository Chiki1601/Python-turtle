#flag of Indonesia
from turtle import *

speed(0)
setup(800, 500)

penup()
goto(-400, 250)
pendown()

# Red rectangle
color("red")
begin_fill()
forward(800)
right(90)
forward(250)
right(90)
forward(800)
end_fill()

hideturtle()
done()
