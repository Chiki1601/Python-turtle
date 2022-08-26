#awesome design 50

import turtle as t 
import colorsys 

t.bgcolor("black")
t.speed(0)
h = 0
for i in range(250):
    t.width(i//100+1)
    c = colorsys.hsv_to_rgb(h,1,1)
    t.pencolor(c)
    t.rt(59)
    t.circle(i*0.6,180)
    t.lt(60)
    t.circle(i,90)
    h+= 0.004
    
t.done()
