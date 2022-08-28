#flag of Itali 
from turtle import *

speed(0)
setup(800, 500)

# Move to start position
penup()
goto(-400, 250)
pendown()

# Green
color("green")
begin_fill()
forward(267)
right(90)
forward(500)
right(90)
forward(267)
end_fill()

# White
color("white")
begin_fill()
right(180)
forward(267)
left(90)
forward(500)
right(90)
forward(267)
right(90)
forward(500)
end_fill()

# Red
color("red")
begin_fill()
left(90)
forward(267)
left(90)
forward(500)
left(90)
forward(267)
end_fill()

hideturtle()
done()
