#awesome design 75 in Python

import turtle as t
import colorsys

t.bgcolor("black")
t.speed(0)
h = 0
t.bk(50)
def design(ang):
    t.circle(60+i,90)
    t.lt(ang)
    t.circle(60+i,90)
    
for i in range(300):
    c = colorsys.hsv_to_rgb(h,0.8,1)
    t.pencolor(c)
    t.circle(i,50)
    design(95)
    t.circle(100,90)
    design(53)
    h += 0.005
    
t.done()
