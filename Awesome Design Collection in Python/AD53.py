#awesome Design 53


import turtle as t 
import colorsys 

t.bgcolor("black")
t.speed(0)
h = 0


t.pu()
t.goto(-100,0)
t.pd()
for i in range(250):
    t.width(i//100+1)
    c = colorsys.hsv_to_rgb(h,1,1)
    t.pencolor(c)
    t.lt(89)
    t.circle(-120,90)
    t.rt(90)
    t.fd(i)
    h+=0.005
    
t.done()
