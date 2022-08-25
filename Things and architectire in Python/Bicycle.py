#bucycle effect
import turtle as t
import time
def Wheel(x,y,tr):
    t.pensize(1)
    r = 30
    a = 20
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.seth(tr)
    for i in range(0,360,a):
        t.left(a)
        t.fd(r)
        t.backward(r)
    t.penup()
    t.goto(x,y-r)
    t.pendown()
    t.seth(0)
    t.pensize(2)
    t,circle(r)
    
def Other(x,y,tr):
    t.pensize(2)
    t.penup()
    t.goto(x-60,0)
    t.seth(45)
    t.pendown()
    t.fd(70)
    t.lt(135)
    t.fd(60)
    t.lt(45)
    t.fd(70)
    t.lt(135)
    t.fd(60)
    t.lt(105)
    t.fd(60)
    t.seth(0)
    t.fd(16)
    t.backward(20)
    t.penup()
    t.goto(x,0)
    t.pendown()
    t.lt(100)
    t.fd(70)
    t.lt(100)
    t.fd(12)
    t.backward(24)
    
    t.penup()
    t.goto(x-60,0)
    t.seth(tr)
    t.pendown()
    t.fd(10)
    t.seth(0)
    t.fd(4)
    t.backward(8)
    
t.screensize()
t.setup(width= 1000,height= 500)
t.speed(1)
Wheel(-60,0,0)
Wheel(60,0,0)
Other(60,0,90)
t.hideturtle()

tr = 0
for x in range(-60,800,1):
    t.tracer(False)
    t.clear()
    Wheel(x,0,tr)
    Wheel(x+120,0,tr)
    Other(x+120,0,tr)
    t.hideturtle()
    t.tracer(True)
    tr -= 1
    time.sleep(0.001)
    
t.done()
