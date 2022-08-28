#flag of Luxemburg
from turtle import *

speed(0)
setup(800, 500)

# Move to start position
penup()
goto(-400, 250)
pendown()

# Red
color("red")
begin_fill()
forward(800)
right(90)
forward(167)
right(90)
forward(800)
end_fill()

left(90)
forward(167)

# Blue
color("dodgerblue")
begin_fill()
forward(167)
left(90)
forward(800)
left(90)
forward(167)
end_fill()

hideturtle()
done()
