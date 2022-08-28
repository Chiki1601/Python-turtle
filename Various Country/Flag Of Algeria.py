#flag of Algeria
import turtle

turtle.bgcolor("white")
t = turtle.Turtle()
t.speed(0.5)

width = 600
height = 300

t.up()
t.goto(-width//2, height//2)
t.down()
t.color("black", "green")
t.begin_fill()
for i in range(4):
    t.fd(width//2)
    t.right(90)
t.end_fill()

t.up()
t.goto(0, height//2)
t.down()
t.color("black", "white")
t.begin_fill()
for i in range(4):
    t.fd(width//2)
    t.right(90)
t.end_fill()

t.color("red", "red")
t.left(120)
t.up()
t.goto(65, 40)
t.down()
t.begin_fill()
t.circle(80, 300)
t.right(10)
t.circle(61, -285)
t.end_fill()
t.up()

t.goto(0, 10)
t.down()
t.setheading(0)
t.right(15)
t.begin_fill()
for i in range(5):
    t.fd(40)
    t.right(144)
t.end_fill()

t.hideturtle()
turtle.done()
