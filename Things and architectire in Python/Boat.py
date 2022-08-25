from turtle import *

setup(800, 500)
speed(0)

# Sky
bgcolor("lightskyblue")

# Water
penup()
goto(-400, -150)
pendown()
color("mediumblue")
begin_fill()
for i in range(2):
    forward(800)
    right(90)
    forward(100)
    right(90)
end_fill()

# Boat
penup()
goto(-200, -80)
pendown()
color("saddlebrown")
begin_fill()
right(45)
forward(100)
left(45)
forward(250)
left(45)
forward(100)
end_fill()

# Mast
penup()
goto(0, -80)
pendown()
color("black")
begin_fill()
left(45)
for i in range(2):
    forward(200)
    left(90)
    forward(10)
    left(90)
end_fill()

# Right Sail
penup()
goto(0, 120)
pendown()
color("white")
begin_fill()
right(130)
forward(250)
right(140)
forward(190)
end_fill()

# Left Sail
penup()
forward(14)
pendown()
begin_fill()
forward(180)
right(139)
forward(240)
end_fill()

# Sun
penup()
goto(-300, 150)
pendown()
color("yellow")
begin_fill()
circle(40)
end_fill()

hideturtle()
