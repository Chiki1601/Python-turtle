#flag of latvia
from turtle import *

speed(0)
setup(800, 500)
bgcolor("darkred")

# Move to start position
penup()
goto(-400, -50)
pendown()

# White stripe
color("white")
begin_fill()
forward(800)
left(90)
forward(100)
left(90)
forward(800)
end_fill()

hideturtle()
done()
