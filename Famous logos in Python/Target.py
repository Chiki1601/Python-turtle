###Target Logo

import turtle

window = turtle.Screen()
window.bgcolor("white")
window.title("coding by Pooja Patel")

v = turtle.Turtle()
v.pencolor("red")
v.speed(1)
v.width(1)
v.hideturtle()

#position of design
v.penup()
v.goto(0, 0)
v.pendown()

#outer Circle
v.dot(500,"#E80018")

v.penup()
v.goto(0,0)
v.pendown()

#inner circle
v.dot(350,"white")

v.penup()
v.goto(0,0)
v.pendown()

#center circle
v.dot(200,"#E80018")
turtle.done()
