#oyo logo in Python
import turtle
t=turtle.Turtle()
t.speed(10)
t.getscreen().bgcolor("red")

def om(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()

t.color("white")
t.begin_fill()
om(-100,100)
t.left(90)
t.circle(100,180)
t.left(25)
t.forward(250)
t.left(132.7)
t.forward(250)
t.end_fill()

t.color("red")
t.begin_fill()
t.backward(100)
t.right(90)
t.forward(150)
t.left(90)
t.forward(100)
t.left(90)
t.forward(150)
t.end_fill()

a=-320
b=158
t.color("red")
t.width(10)
t.right(157.5)
for i in range(6):
    om(a,b)
    t.forward(300)
    b=b-60

t.color("white")
om(-40,-40)
t.width(25)
t.write("OYO",font=("CALLIBRI",50))

t.hideturtle()
turtle.done()
