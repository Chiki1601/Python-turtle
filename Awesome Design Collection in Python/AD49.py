#awesome design 49
import turtle as t 
import colorsys 

t.bgcolor("black")
t.speed(0)
h = 0
for i in range(200):
    t.width(i//100+1)
    c = colorsys.hsv_to_rgb(h,1,1)
    t.pencolor(c)
    h += 0.005
    
    for j in range(4):
        t.fd(i)
        t.lt(45)
        t.circle(i,90)
    t.rt(59)
    
t.done()
