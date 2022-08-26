#awesome Design 41
import turtle as t 
import colorsys 

t.bgcolor("black")
t.speed(11)

h = 0
n =90
for i in range(300):
    c = colorsys.hsv_to_rgb(h,0.6,1)
    t.pencolor(c)
    t.width(i//100+1)
    t.rt(150)
    t.fd(i)
    t.circle(i,60)
    t.lt(149)
    t.fd(i)
    t.circle(i,30)
    t.rt(50)
    t.fd(i)
    t.circle(i,60)
    t.lt(59)
    t.fd(i)
    t.circle(i,60)
    h+= 1/n
    
t.done()    
               
