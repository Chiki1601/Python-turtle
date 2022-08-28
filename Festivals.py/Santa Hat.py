#santa HAT
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

# Red Part of Hat
penup()
goto(-120, -60)
pendown()
color("red")
begin_fill()
for i in range(3):
    forward(250)
    left(120)
end_fill()

# Pom Pom
penup()
goto(5, 140)
pendown()
color("white")
begin_fill()
circle(20)
end_fill()

# Trim on Hat
penup()
goto(-105, -80)
pendown()
begin_fill()
for i in range(12):
    circle(20)
    penup()
    forward(20)
    pendown()
end_fill()

# Message
penup()
goto(-150, -200)
pendown()
write("HAPPY CHRISTMAS", font=("Arial", 25, "bold"))

done()
