#Awesome Design 72 in Python

import turtle as t
import colorsys
t.pensize(1)
t.bgcolor("black")
t.tracer(500)
h = 0.5
t.ht()
t.goto(0,0)
for i in range(170):
    c = colorsys.hsv_to_rgb(h,1,1)
    t.color(c)
    t.begin_fill()
    t.fd(i)
    t.lt(15)
    for j in range(50):
        t.fd(i)
        for k in range(12):
            t.lt(198)
            h += 0.008
    t.end_fill()
t.done()   
