#awesome design 52

import turtle as t 
import colorsys 

t.bgcolor("black")
t.speed(0)
h = 0

for i in range(250):
    t.width(i//100+2)
    c = colorsys.hsv_to_rgb(h,1,0.9)
    t.pencolor(c)
    
    t.rt(179)
    t.circle(-i,180)
    t.fd(i*0.5)
    t.circle(i*0.5,180)
    t.fd(i)
    h += 0.005
    
t.done()
