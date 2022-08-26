#awesome design 47

import turtle as t 
import colorsys 

t.bgcolor("black")
t.speed(12)

c = [colorsys.hsv_to_rgb(h/10,0.7,0.9)for h in range(12)]
k = 0
while(k<300):
    t.pencolor(c[k%12])
    t.width(i//100+1)
    t.pu()
    t.lt(45)
    t.fd(k*1.5)
    t.rt(90)
    t.fd(k*1.5)
    t.pd()
    t.lt(45)
    t.circle(k,-30)
    t.rt(90)
    t.circle(k,-30)
    k +=1
    
t.done()
