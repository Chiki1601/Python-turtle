#domino's logo in Python

import turtle as t

t.color("blue")

t.rt(45)
def square():
    t.begin_fill()
    for  i in range(4):
        t,fd(100)
        t.rt(90)
    t.end_fill()
    
square()
t.penup()
t.goto(5,5)
t.pd()
t.color("#e8002f")
t.lt(90)
square()
t.color("White")
def circle(x,y):
    t.pu()
    t.goto(x,y)
    t.pd()
    t.begin_fill()
    t.circle(15)
    t.end_fill()
circle(87,-7)
circle(-15,-83)
circle(37,-83)
t.pencolor("#006393")
t.pu()
t.goto(-100,-230)
t.pd()
t.write("Domino's Pizza logo",font=("future",40,"bold"))
t.ht()
t.done()
