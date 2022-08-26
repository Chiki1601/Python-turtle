#awesome design 46

import turtle as t 
import colorsys 

t.bgcolor("black")
t.speed(100)

h = 0
n =66
for i in range(300):
    c = colorsys.hsv_to_rgb(h,1,0.9)
    t.pencolor(c)
    t.width(i//80)
    t.lt(90+i)
    t.fd(i*0.3)
    t.circle(i,30)
    t.rt(90+i)
    t.fd(i*0.3)
    t.lt(59)
    t.fd(i*0.4)
    t.lt(90-i)
    t.fd(i*0.3)
    t.circle(i,30)
    t.rt(90-i)
    t.fd(i*0.3)
    t.rt(29)
    t.fd(i*0.4)
    h+= 1/n
    
t.done()
