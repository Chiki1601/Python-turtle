#awesome Design 44
import turtle as t 
import colorsys 

t.bgcolor("black")
t.speed(0)
c = [colorsys.hsv_to_rgb(h*0.14,1,0.8)for h in range(6)]
for i in range(100):
    t.width(i//100+1)
    t.pu()
    t.pencolor(c[i%5])
    t.fd(i*2)
    t.pd()
    t.circle(i,-10)
    t.lt(59)
    t.pu()
    t.fd(i*2)
    t.pd()
t.done()
