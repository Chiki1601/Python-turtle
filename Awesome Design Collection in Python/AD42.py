#awesome Design 42

import turtle as t 
import colorsys 

t.bgcolor("black")
t.speed(12)

h = 0
n =36
for i in range(100):
    c = colorsys.hsv_to_rgb(h,0.6,1)
    t.pencolor(c)
    t.width(i//100+1)
    t.pu()
    t.lt(90*i)
    t.circle(i,-45)
    t.fd(i*6)
    t.circle(i,30)
    t.pd()
    
    
    while(i!=0):
        t.lt(i)
        t.fd(i)
        t.rt(90+i)
        t.backward(i*2)
        i -=1
        
    h+= 5/n
    
t.done()    
