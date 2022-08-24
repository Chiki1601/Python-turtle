#audi logo in Python

import turtle
 
Pooja = turtle.Turtle()
Pooja.pensize(4)
 
for i in range(4):
  Pooja.penup()
  Pooja.goto(i*70, 0)
  Pooja.pendown()
  Pooja.circle(50)

turtle.done()
