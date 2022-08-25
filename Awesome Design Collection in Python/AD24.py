#Awesome Design 24
import turtle as t
import colorsys as c
t.bgcolor("black")
t.speed(0)
h = 0.5
n = 1
for i in range(160):
    c = colorsys.hsv_to_rgb(h,1,0.9)
    h += 1/n
    t.color(c)
    t.lt(145)
    for i in range(5):
        t.fd(300)
        t.lt(150)
        
t.done()
