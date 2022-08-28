#christmas Gift

from turtle import *

speed(0)

# Background
penup()
goto(0, -300)
pendown()
color("green")
begin_fill()
circle(300)
end_fill()

# Lid on gift
penup()
goto(-180, 20)
pendown()
color("red")
begin_fill()
for i in range(2):
    forward(360)
    left(90)
    forward(60)
    left(90)
end_fill()

# Bottom of gift
penup()
goto(-160, 0)
pendown()
begin_fill()
for i in range(2):
    forward(320)
    right(90)
    forward(210)
    right(90)
end_fill()

# Green line through middle of gift
penup()
goto(-10, 80)
pendown()
color("green")
begin_fill()
for i in range(2):
    forward(20)
    right(90)
    forward(290)
    right(90)
end_fill()

# Right ribbon
penup()
goto(10, 100)
pendown()
pensize(10)
color("red")
for i in range(90):
    forward(1)
    left(0.4)
for i in range(90):
    forward(1)
    left(2)
for i in range(90):
    forward(1)
    left(0.4)



# Left ribbon
penup()
goto(-10, 100)
pendown()
right(70)
for i in range(90):
    forward(1)
    right(0.4)
for i in range(90):
    forward(1)
    right(2)
for i in range(90):
    forward(1)
    right(0.4)

# Message
penup()
goto(-160, 210)
pendown()
color("white")
write("Christmas Gift", font=("Arial", 22, "bold"))

hideturtle()
done()
