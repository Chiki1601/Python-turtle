#awesome design 67

from operator import lt
from tkinter import mainloop
import  turtle as t


t.pencolor("gold")
t.bgcolor("dark blue")
t.pensize(10)
t.hideturtle()
t.speed(10)
for i in range(4):

    t.fillcolor("gold")
    t.begin_fill()
    t.circle(200,90)
    t.backward(400)
    t.circle(200,90)
    t.end_fill()
    t.rt(90)
    
t.penup()
t.lt(90)
t.fd(50)
t.lt(90)
t.fd(50)
t.rt(90)
t.pendown()
t.pencolor("black")

t.fillcolor("black")
t.begin_fill()
t.circle(100,90)
t.rt(90)
t.circle(-100,-90)

t.end_fill()
t.penup()
t.rt(90)
t.backward(50)
t.rt(90)
t.fd(100)
t.rt(90)
t.backward(50)
t.lt(90)
t.pendown()



t.fillcolor("black")
t.begin_fill()

t.circle(100,90)
t.rt(90)
t.circle(-100,-90)

t.end_fill()

t.penup()
t.backward(50)
t.rt(90)
t.backward(100)
t.rt(90)
t.fd(50)
t.rt(90)
t.pendown()


t.fillcolor("White")
t.pencolor("white")
t.begin_fill()

t.circle(100,90)
t.rt(90)
t.circle(-100,-90)

t.end_fill()


t.penup()
t.backward(50)
t.rt(90)
t.backward(100)
t.rt(90)
t.backward(50)
t.rt(90)
t.pendown()


t.fillcolor("White")
t.pencolor("white")
t.begin_fill()

t.circle(-100,90)
t.rt(90)
t.circle(-100,90)

t.end_fill()


t.mainloop()
