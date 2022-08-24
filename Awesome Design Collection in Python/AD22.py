#Awesome design 22

import turtle
import turtle
t= turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")
t.pencolor("red")
t.speed(0)
for i in range(150):
    t.circle(190-i,90)
    t.lt(90)
    t.circle(190-i,90)
    t.lt(18)
    
turtle.done()
