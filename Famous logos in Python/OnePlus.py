#one plus logo in Python
import turtle

t = turtle.Turtle()
t.getscreen().bgcolor("red")

t.penup()
t.goto(-240,0)
t.pendown()
t.color("white")
t.begin_fill()
t.forward(60)
t.left(90)
t.forward(35)
t.right(90)
t.forward(10)
t.right(90)
t.forward(45)
t.right(90)
t.forward(80)
t.right(90)
t.forward(90)
t.right(90)
t.forward(40)
t.right(90)
t.forward(10)
t.right(90)
t.forward(30)
t.left(90)
t.forward(70)
t.end_fill()

t.penup()
t.goto(-200,20)
t.pendown()
t.write("+",font=("calbri",25,"bold"))

t.penup()
t.goto(-228,-5)
t.pendown()
t.write("1",font=("calbri",20,"bold"))

t.penup()
t.goto(-140,0)
t.pendown()
t.write("ONEPLUS",font=("calbri",25,"bold"))





t.hideturtle()
turtle.done()
