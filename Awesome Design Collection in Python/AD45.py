#Awesome Design 45

import turtle as t 
import colorsys 

t.bgcolor("black")
t.speed(11)
c = [colorsys.hsv_to_rgb(h*0.3,1,0.9)for h in range(6)]
for i in range(100):
    t.width(i//100+1)
    t.pu()
    t.pencolor(c[i%5])
    t.fd(i*2)
    t.lt(269*3.14+90)
    t.pd()
    t.circle(i,90)
    t.rt(3.14*44+69)
    t.fd(10)
    t.circle(i,10)
t.done()
