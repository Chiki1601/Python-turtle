import turtle
import random

t = turtle.Turtle()

t.speed(9)
t.pensize(3)

t.showturtle()
wn = turtle.Screen()
wn.bgcolor("Black")

t.pencolor("red")

def myPosition(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()

myPosition(-13,170)

t.forward(50)
t.left(90)
t.forward(10)
t.left(90)
t.forward(100)
t.left(90)
t.forward(10)
t.left(90)
t.forward(50)

turtle.pencolor("darkorange")

myPosition(-13,185)
t.forward(35)
t.left(90)
t.forward(10)
t.left(90)
t.forward(70)
t.left(90)
t.forward(10)
t.left(90)
t.forward(35)

t.pencolor("gold")

myPosition(-13,200)

t.forward(25)
t.left(90)
t.forward(10)
t.left(90)
t.forward(50)
t.left(90)
t.forward(10)
t.left(90)
t.forward(25)

t.pencolor("yellow")

myPosition(-13,215)
t.pencolor("red")

for i in range(12):
    t.forward(5)
    t.left(30)
myPosition(-13,160)
t.right(90)
t.left(15)
t.forward(10)
t.right(15)
t.forward(15)
t.right(15)
t.forward(10)
t.left(15)
t.right(165)
t.forward(10)
t.right(15)
t.forward(15)
t.right(15)
t.forward(10)
t.left(15)

t.pencolor("gold")
myPosition(-20,-180)

t.left(90)
for i in range(7):
    t.right(20)
    t.forward(20)
t.forward(10)
t.left(5)
t.forward(5)
t.left(5)
t.forward(10)
t.left(5)
t.forward(15)
t.left(30)
t.forward(10)
t.left(5)
t.forward(10)

for i in range(2):
    t.left(20)
    t.forward(6)
t.right(20)
t.forward(60)
t.left(100)
t.forward(20)

for i in range(8):
    t.right(20)
    t.forward(1)
t.forward(20)
t.left(50)
t.forward(30)

for i in range(4):
    t.left(20)
    t.forward(10)
t.forward(20)
t.left(95)
t.forward(50)
t.right(155)
t.forward(80)
t.right(120)
turtle.forward(80)

for i in range(4):
    t.right(20)
    t.forward(15)
t.forward(25)
t.right(30)
t.forward(5)
t.left(150)
t.forward(5)
t.right(118)
t.forward(80)

for i in range(3):
    t.right(20)
    t.forward(20)
t.forward(20)

for i in range(4):
    t.left(24)
    t.forward(25)
myPosition(-1,-130)
t.left(15)

for i in range(7):
    t.right(30)
    t.forward(10)

t.left(8)
for i in range(4):
    t.right(24)
    t.forward(20)

for i in range(3):
    t.left(20)
    t.forward(25)
t.left(10)
t.forward(60)
t.right(20)
t.forward(50)

for i in range(3):
    t.right(22)
    t.forward(15)
t.right(15)
t.forward(55)
t.right(105)
t.forward(70)
t.right(160)
t.forward(50)
t.left(80)
turtle.forward(20)

for i in range(3):
    t.left(23)
    t.forward(15)
t.left(3)
t.forward(20)
t.left(90)
t.forward(20)

for i in range(3):
    t.right(50)
    t.forward(3)
t.forward(15)
t.left(90)
t.forward(60)

for i in range(4):
    t.right(10)
    t.forward(15)
t.forward(23)
t.right(15)
t.forward(5)
t.right(15)
t.forward(8)

for i in range(6):
    t.left(15)
    t.forward(10)
t.left(160)
t.forward(20)
t.right(40)
t.forward(5)

for i in range(5):
    t.right(20)
    t.forward(5)
t.forward(10)

myPosition(-330,-250)
t.pencolor("red")

t.write('Happy Ganesh Chaturthi', font=("Bradley Hand ITC", 40, "bold"))
turtle.dot
turtle.done()
