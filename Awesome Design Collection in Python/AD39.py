#awesome Design 39

import turtle as t 
import colorsys

t.bgcolor("black")

t.speed(0)

h = 0
for i in range(130):
    t.width(i//100+1)
    c = colorsys.hsv_to_rgb(h,1,1)
    t.pencolor(c)
    h += 0.007
    
    for j in range(5):
        t.fd(i-5)
        t.lt(30)
        t.rt(8)
    t.lt(115)
    
t.done()
