#zomato

import turtle
t=turtle.Turtle()
t.speed(2)
t.color("black")
t.fillcolor("red2")
t.penup()
t.goto(-100,120)
t.pendown()
t.begin_fill()
for i in range(4):
    t.forward(280)
    t.right(90)
t.end_fill()
t.penup()
t.goto(-60,-40)
t.pendown()

t.color("white")
t.write("zomato",font=("Times",15,"bold"))
t.hideturtle()
turtle.done()
