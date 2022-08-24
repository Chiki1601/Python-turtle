#awesome design 23

import turtle as t 
import colorsys

t.bgcolor("black")
t.pensize(2)
t.setpos(-40,30)
t.tracer(10)
h = 0.5

for i in range(400):
    c = colorsys.hsv_to_rgb(h,1,1)
    t.pencolor(c)
    h += 0.004
    t.fd(i)
    t.rt(31)
    t.fd(i)
    t.rt(150)
    
    
t.done()
