#Captain America Shield


import turtle

def circle(radius,color):
    turtle.color(color)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()
    
turtle.goto(-30,-280)
circle(300,'red')

turtle.goto(-30,-240)
circle(260,'white')

turtle.goto(-30,-200)
circle(220,'red')

turtle.goto(-30,-160)
circle(180,'blue')

turtle.goto(-200,75)
turtle.begin_fill()
turtle.color('white')

for i in range(5):
    turtle.forward(340)
    turtle.right(144)
turtle.end_fill()

turtle.hideturtle()
turtle.done()
