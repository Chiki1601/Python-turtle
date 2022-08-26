#awesome Design 32

import turtle as t
import colorsys
t.Screen().bgcolor("black")
h = 0
t.speed(0)
for i in range(220):
    t.width(i//100)
    c = colorsys.hsv_to_rgb(h,0.8,1)
    t.pencolor(c)
    t.rt(119)
    t.circle(-i*0.5,120)
    t.circle(i*0.5,120)
    t.circle(-i*0.3,90)
    t.circle(i*0.3,90)
    h += 0.006
t.done()
