#Awesome Design 65
import turtle as t
import colorsys

t.hideturtle()
t.speed(0)
t.bgcolor("black")
h = 0
t.pensize(3)

def Design(ang):
    t.circle(60-i,90)
    t.lt(ang)
    t.circle(60+i,90)

t.pu()
t.goto(40,0)
t.pd()
for i in range(160):
    c= colorsys.hsv_to_rgb(h,0.8,1)
    t.pencolor(c)
    Design(90)
    Design(90)
    t.pu()
    Design(60)
    Design(60)
    t.pd()
    h += 0.01
t.done()

done()
