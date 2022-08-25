#awesome design 30
import turtle
import time
turtle.bgcolor('black')
turtle.speed(0)
turtle.pensize(10)
turtle.setup(700,700)
color = ('orange','blue','limegreen','magenta')
for i in range(100):
    turtle.pencolor(color[i%4])
    turtle.width(3)
    turtle.forward(i)
    turtle.right(45)
    turtle.forward(i*2)
    turtle.right(45)

turtle.hideturtle()
time.sleep(3)
