#Christmas decoration
from turtle import *

speed(0)

# Background
bgcolor("indigo")

# Chain
penup()
goto(0, 250)
pendown()
color("darkkhaki")
pensize(10)
right(90)
forward(100)

# Attachment
pensize(1)
right(90)
back(20)
begin_fill()
for i in range(2):
    forward(40)
    left(90)
    forward(10)
    left(90)
end_fill()

# Red bauble
penup()
goto(0, 140)
pendown()
color("crimson")
begin_fill()
circle(200)
end_fill()

# Gold zigzag
penup()
goto(176, 30)
pendown()
color("gold")
pensize(3)
left(45)
for i in range(5):
    forward(50)
    right(90)
    forward(50)
    left(90)

# Green circles
penup()
goto(-160, -65)
pendown()
color("limegreen")
left(135)
begin_fill()
for i in range(5):
    circle(10)
    penup()
    forward(80)
    pendown()
end_fill()

# Gold zigzag 2
penup()
goto(-185, -135)
pendown()
color("gold")
left(45)
for i in range(5):
    forward(50)
    right(90)
    forward(50)
    left(90)
forward(35)    

# Stars at top
penup()
goto(-105, 80)
pendown()
pensize(1)
color("aliceblue")
setheading(0)
for i in range(3):
    begin_fill()
    for i in range(5):
        forward(30)
        right(144)
    end_fill()
    penup()
    forward(90)
    pendown()

# Stars at bottom
penup()
goto(-105, -180)
pendown()
setheading(0)
for i in range(3):
    begin_fill()
    for i in range(5):
        forward(30)
        right(144)
    end_fill()
    penup()
    forward(90)
    pendown()

# Message
penup()
goto(-180, 270)
pendown()
color("white")
write("SEASONS GREETINGS", font=("Arial", 24, "bold"))

hideturtle()
done()
