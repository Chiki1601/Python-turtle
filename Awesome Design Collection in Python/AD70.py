#awesome Design 70

import turtle as t
import colorsys
t.speed(10)
t.bgcolor("black")
h = 0.4
t.pensize(5)
t.shape("turtle")
t.goto(-300,100)
for i in range(10):
    color=("red","blue")
    t.color(color[i%2])
    t.begin_fill()
    for i in range(4):
        t.rt(109)
        t.circle(140,-100)
        
    t.rt(10)
    t.lt(90)
    h +=0.009
    t.end_fill()
    t.ht()
    
t.done()
