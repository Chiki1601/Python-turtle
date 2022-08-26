#awesome Design 43
import turtle as t 
import colorsys 

t.bgcolor("black")
t.speed(12)

h = 0
n =100
t.pu()
t.goto(180,-200)
t.pd()
t.pu()
t.lt(119)
t.fd(350)
t.pd()
k = 0 

while(k<250):
    c = colorsys.hsv_to_rgb(h,0.6,1)
    t.pencolor(c)
    t.width(k//100+1)
    t.fillcolor(c)
    t.lt(59)
    t.fd(k)
    t.begin_fill()
    t.circle(k*0.17)
    t.end_fill()
    t.fd(k)
    t.circle(k,-9)
    
    k += 1
    h += 10/n
    
t.done()
