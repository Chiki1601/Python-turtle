#awesome Design 37

import turtle as t 
import colorsys

t.bgcolor("black")
t.pensize(2)
t.speed(0)

h = 0
for i in range(300):
    
    c = colorsys.hsv_to_rgb(h,1,1)
    t.pencolor(c)
    t.lt(89)
    t.begin_fill()
    t.circle(i,60)
    t.end_fill()
    h+=0.005
    
    
t.done()
