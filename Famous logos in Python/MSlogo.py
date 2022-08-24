import turtle

turtle.bgcolor('Black')
turtle.colormode(255)

def square():
    for i in range(4):
        turtle.forward(200)
        turtle.right(90)
    turtle.left(90)
    
    
#yellow box
turtle.penup()
turtle.goto(100,-150)
turtle.pendown()
turtle.color(255,187,0)
turtle.begin_fill()
square()
turtle.end_fill()

#green box
turtle.penup()
turtle.goto(100,-70)
turtle.pendown()
turtle.color(124,187,0)
turtle.begin_fill()
square()
turtle.end_fill()

#red box
turtle.penup()
turtle.goto(-70,100)
turtle.pendown()
turtle.color(246,83,20)
turtle.begin_fill()
square()
turtle.end_fill()

#blue box
turtle.penup()
turtle.goto(-100,-150)
turtle.pendown()
turtle.color(0,161,241)
turtle.begin_fill()
square()
turtle.end_fill()


turtle.done()
