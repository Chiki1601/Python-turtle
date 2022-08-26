#awesome Design 36

import turtle as t 
import colorsys

t.bgcolor("black")
t.pensize(2)
t.speed(0)

h = 0
for i in range(400):
    
    c = colorsys.hsv_to_rgb(h,1,1)
    t.pencolor(c)
    t.lt(120)
    t.pu()
    t.fd(i)
    t.pd()
    t.rt(59)
    t.circle(40,60)
    h+=0.005
    
    
t.done()
