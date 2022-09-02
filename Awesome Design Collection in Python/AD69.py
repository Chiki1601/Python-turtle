#Awesome Design 69

import turtle as t
import colorsys
t.setup(1537)
t.tracer(100)
t.bgcolor("black")
h = 0.0
t.pensize(30)


for i in range(800):
    c = colorsys.hsv_to_rgb(h,1,1)
    t.pencolor(c)
    t.up()
    t.goto(0,0)
    t.fd(i)
    t.down()
    
    
    
    def dot():
        t.up()
        t.circle(100,100)
        t.down()
        t.lt(145)
        t.circle(70,1)
    dot()
    h +=0.008
    t.ht()
t.done()
