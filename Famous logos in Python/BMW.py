#bmw logo in Python

import turtle as t
t.begin_fill()
t.fillcolor('#008ac9')
for i in range(50):
    t.forward(4)
    t.left(2)
t.right(-80)
t.forward(116)
t.right(-90)
t.forward(132)
t.end_fill()
t.penup()
t.pendown()
t.right(90)
for i in range(50):
    t.forward(4)
    t.left(-2)

t.right(80)
t.forward(116)
t.forward(-116)
t.right(90)
t.begin_fill()
t.fillcolor('#008ac9')
for j in range(45):
    t.forward(-4)
    t.left(-2)

t.right(-90)
t.forward(116)
t.end_fill()
t.right(180)
t.forward(116)
t.right(90)
for i in range(47):
    t.forward(4)
    t.left(-2)

t.done()
x = t.Turtle()
