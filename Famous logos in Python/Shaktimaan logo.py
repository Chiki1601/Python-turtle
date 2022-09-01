#shaktimaan logo
import turtle

turtle.bgcolor("red")
def drawshape(turtle,radius):
    turtle.circle(radius,extent=60)
    turtle.left(120)
    turtle.circle(radius,extent=60)

def drawflower():

    petal=turtle.Turtle()
    petal.color("yellow")
    petal.speed(0)
    petal.pensize(4)
    no_of_petals=15
    radius=145
    petal.begin_fill()
    for i in range(no_of_petals):
        drawshape(petal,radius)
        petal.left(360 /no_of_petals )
    petal.end_fill()

drawflower()

#draw the main round circle of Shaktiman Logo
turtle.pensize(4)
turtle.color("yellow","red")
turtle.goto(0,-94)
turtle.pendown()
turtle.begin_fill()
turtle.circle(95)
turtle.end_fill()


#draw the first triangle
turtle.color("yellow")
turtle.begin_fill()
turtle.left(60)
turtle.forward(160)
turtle.left(120)
turtle.forward(160)
turtle.left(120)
turtle.forward(160)
turtle.end_fill()

#draw the second Triangle
turtle.penup()
turtle.color("red")
turtle.goto(-0,-70)
turtle.pendown()
turtle.begin_fill()
turtle.left(120)
turtle.forward(120)
turtle.left(120)
turtle.forward(120)
turtle.left(120)
turtle.forward(120)
turtle.end_fill()
turtle.penup()

#Draw the third triangle
turtle.color("yellow","yellow")
turtle.goto(80,-43)
turtle.pendown()
turtle.setheading(0)
turtle.left(120)
turtle.forward(160)
turtle.setheading(270)
turtle.right(30)
turtle.forward(160)
turtle.setheading(0)
turtle.forward(160)

#draw the fourth triangle
turtle.begin_fill()
turtle.backward(15)
turtle.left(90)
turtle.forward(10)
turtle.left(30)
turtle.forward(135)
turtle.right(30)
turtle.forward(13)
turtle.end_fill()
turtle.begin_fill()
turtle.backward(15)
turtle.left(150)
turtle.forward(138)
turtle.right(25)
turtle.forward(15)
turtle.end_fill()
turtle.pensize(9)
turtle.backward(10)
turtle.setheading(0)
turtle.forward(138)
turtle.penup()

#draw the s letter of shaktiman
turtle.pensize(2)
turtle.goto(-28,-25)
turtle.pendown()
turtle.left(20)
turtle.begin_fill()
turtle.forward(10)
turtle.left(40)
turtle.forward(55)
turtle.right(30)
turtle.forward(20)
turtle.right(100)
turtle.forward(10)
turtle.right(80)
turtle.forward(15)
turtle.left(30)
turtle.forward(55)
turtle.right(27)
turtle.forward(20)
turtle.end_fill()

turtle.hideturtle()
turtle.done()
