#Awesome Design 73 in Python

import turtle as t
import colorsys
t.pensize(1)
t.bgcolor("black")
t.speed(0)
h = 0
for i in range(150):
    t.width(i//100+2)
    c = colorsys.hsv_to_rgb(h,1,0.8)
    t.color(c)
    t.lt(90)
    t.fd(i)
    t.circle(i)
    t.rt(150)
    t.fd(i)
    h += 0.015
    
t.ht()
t.done()
