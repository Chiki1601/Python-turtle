#flag of Iceland
from turtle import *

speed(0)
setup(800, 500)
bgcolor("royalblue")

penup()
goto(-400, -50)
pendown()

# White Cross
color("white")
begin_fill()
forward(800)
left(90)
forward(100)
left(90)
forward(800)
end_fill()

# Move to next position for the white cross
penup()
goto(-100, -250)
pendown()

begin_fill()
forward(100)
right(90)
forward(500)
right(90)
forward(100)
end_fill()

# Move to the starting red cross position
penup()
goto(-400, -25)
pendown()

# Red cross
color("red")
begin_fill()
forward(800)
left(90)
forward(50)
left(90)
forward(800)
end_fill()

penup()
goto(-125, -250)
pendown()

begin_fill()
forward(50)
right(90)
forward(500)
right(90)
forward(50)
end_fill()

hideturtle()
done()
