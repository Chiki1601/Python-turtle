#awesome Design 33

import turtle as t
import colorsys
t.width(20)
h = 0
t.tracer(200)
t.bgcolor("black")
t.setup(1537,865)



for i in range(2000):
    c = colorsys.hsv_to_rgb(h,1,1)
    h += 0.01
    t.pencolor(c)
    t.begin_fill()
    t.fd(i)
    t.rt(60)
    t.fd(i)
    t.circle(i,-120)
    t.fd(i)
    t.rt(180)
    t.circle(-i,-60)
    t.end_fill()

t.done()
