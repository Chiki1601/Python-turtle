#om  

import turtle
import colorsys

turtle.Screen().bgcolor("black")

t = turtle.Pen()
t.speed(0)

t.pencolor("#de4721")
def go(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()

go(-200,50)

t.fillcolor("#de4721")
t.begin_fill()
t.seth(-90)
t.circle(200,70)
t.circle(70,180)
t.seth(110)
t.forward(30)
t.seth(0)
t.circle(60,100)
t.circle(80,120)
t.seth(130)
t.forward(30)
t.seth(50)
t.circle(-100,120)
t.circle(-90,90)
t.seth(-19)
t.circle(-60,50)
t.seth(0)
t.circle(60,90)
t.circle(-70,180)
t.forward(50)
t.circle(-90,120)
t.seth(-15)
t.circle(90,90)
t.seth(90)
t.forward(50)
t.circle(40,180)
t.circle(-75,90)
t.seth(-65)
t.circle(-90,132)
t.circle(-210,80)
t.end_fill()

go(30,210)
t.begin_fill()
t.seth(-70)
t.circle(120,110)
t.seth(120)
t.forward(40)
t.seth(-140)
t.circle(-120,90)
t.end_fill()

go(140,220)
t.begin_fill()
t.circle(25)
t.end_fill()

turtle.done()
