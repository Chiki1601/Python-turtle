#awesome Design 54
import turtle as t
import colorsys
t.bgcolor("black")

t.Turtle()
t.speed(0)
h=0
t.pensize(2)

for i in range(260):
    c = colorsys.hsv_to_rgb(h,0.8,1)
    t.pencolor(c)
    t.fillcolor(c)
    t.circle(i,-90)
    t.lt(54)
    t.circle(-i,90)
    h+= 0.006
    
t.done()
