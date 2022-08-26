#awesome design 48

import turtle as t 
import colorsys 

t.bgcolor("black")
t.speed(0)
h = 0
for i in range(150):
    t.width(i//100+1)
    c = colorsys.hsv_to_rgb(h,1,1)
    t.pencolor(c)
    t.lt(9)
    t.fd(i*2)
    t.circle(-i*1.5,180)
    t.backward(i*2)
    h += 0.007
    
t.done()
