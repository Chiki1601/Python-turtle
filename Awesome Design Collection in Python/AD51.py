#awesome design 51

import turtle as t 
import colorsys 

t.bgcolor("black")
t.speed(11)
h = 0
n = 40
for i in range(300):
    t.width(i//100+1)
    c = colorsys.hsv_to_rgb(h,0.8,1)
    t.pencolor(c)
    t.lt(90+i)
    t.fd(i*0.3)
    t.circle(i,30)
    t.rt(90+i)
    t.fd(i*0.3)
    t.circle(i,30)
    t.lt(59)
    t.fd(i*0.4)
    h+= 3/n
    
t.done()
