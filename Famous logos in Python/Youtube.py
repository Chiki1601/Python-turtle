####Youtube

import turtle

window = turtle.Screen()
window.bgcolor("white")
window.title("coding by Pooja Patel")

p = turtle.Turtle()
p.pencolor("white")
p.speed(0)
p.width(3)
p.fillcolor("red")
p.hideturtle()

# position of design
p.penup()
p.goto(-10, 120)
p.pendown()

#youtube box code
def curve1():
    for i in range(30):
        p.right(3)
        p.forward(2)

def curve2():
    for i in range(30):
        p.right(3)
        p.forward(2)

def curve3():
    for i in range(30):
        p.right(3)
        p.forward(2)

def curve4():
    for i in range(30):
        p.right(3)
        p.forward(2)

p.pencolor("#FF0000")
p.begin_fill()
p.forward(100)
curve1()
p.forward(50)
curve2()
p.forward(100)
curve3()
p.forward(50)
curve4()
p.forward(30)
p.end_fill()

p.penup()
p.right(90)
p.forward(30)
p.pendown()


#triangle code
p.fillcolor("white")
p.begin_fill()
p.pencolor("white")
p.pensize(5)
p.forward(60)
p.left(120)
p.forward(60)
p.left(120)
p.forward(60)
p.end_fill()

turtle.done()
