#awesome design 34

import turtle as t
import colorsys as c
t.bgcolor("black")
t.speed(0)
t.width(1)
def square(x):
    for i in range(4):
        t.fd(x)
        t.lt(90)
        
def shape(x):
    t.fd(x)
    t.lt(45)
    t.fd(x)
    t.rt(60)
    t.width(3)
    square(x)
    t.width(1)
    t.rt(165)
    t.fd(x)
    t.lt(45)
    t.fd(x)
h = 0.0
for i in range(90):
    t.color(c.hsv_to_rgb(h,1,1))
    t.circle(50,4)
    t.rt(90)
    shape(70)
    t.rt(135)
    h+=0.0111
    
t.ht()
t.done()
