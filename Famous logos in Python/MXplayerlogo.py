#MX player logo in Python


import turtle

window = turtle.Screen()
window.bgcolor("white")
window.title("coding by Pooja Patel")

v = turtle.Turtle()
v.pencolor("white")
v.speed(0)
v.width(3)
v.fillcolor("blue")
v.hideturtle()

# position of design
v.penup()
v.goto(-10, 120)
v.pendown()

#youtube box code
def curve1():
    for i in range(30):
        v.right(3)
        v.forward(2)

def curve2():
    for i in range(30):
        v.right(3)
        v.forward(2)

def curve3():
    for i in range(30):
        v.right(3)
        v.forward(2)

def curve4():
    for i in range(30):
        v.right(3)
        v.forward(2)

v.pencolor("blue")
v.begin_fill()
v.forward(100)
curve1()
v.forward(50)
curve2()
v.forward(100)
curve3()
v.forward(50)
curve4()
v.forward(30)
v.end_fill()

v.penup()
v.right(90)
v.forward(30)
v.pendown()


#triangle code
v.fillcolor("white")
v.begin_fill()
v.pencolor("white")
v.pensize(5)
v.forward(60)
v.left(120)
v.forward(60)
v.left(120)
v.forward(60)
v.end_fill()

turtle.done()
