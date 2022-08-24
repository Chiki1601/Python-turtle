#Awesome design in Pytohn turtle
import turtle as t
import colorsys as cs

t.bgcolor("black")
t.tracer(10)
t.width(2)

def square(x):
    for i in range(3):
        t.fd(x)
        t.lt(90)
    t.fd(x)
n = 35

for i in range(n):
    t.color(cs.hsv_to_rgb(1-i/n,1-i/n,1))
    for j in range(4):
        square(30+(i*3))
        t.circle(30+(i*3))

t.hideturtle()
t.done()
