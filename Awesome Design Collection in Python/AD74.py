#awesome design 74 in Python

import turtle as t
t.tracer(100)
t.bgcolor("black")
t.pensize(3)
t.goto(40,90)
t.ht()
for i in range(220):
    color = ("red","white","blue")
    t.color(color[i%3])
    t.begin_fill()
    t.fd(i*2)
    t.circle(60,179)
    t.rt(60)
    t.end_fill()

t.done()
