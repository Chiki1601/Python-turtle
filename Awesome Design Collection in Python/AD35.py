#awesome design 35

import turtle as t 
import colorsys

t.bgcolor("black")

t.speed(0)
h = 0
for i in range(260):
    t.width(i//100+1)
    c = colorsys.hsv_to_rgb(h,0.8,1)
    t.pencolor(c)
    t.fillcolor(c)
    t.lt(60)
    t.fd(20)
    t.rt(9)
    t.begin_fill()
    t.circle(-i*0.3,90)
    t.end_fill()
    h+= 0.006
    
t.done()
