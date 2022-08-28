#leaf drawing in Python
import turtle
import random

screen = turtle.Screen()
screen.title('Leaf with Python Turtle')
screen.setup(1000, 1000)
screen.setworldcoordinates(-6, -1, 6, 11)
screen.tracer(0, 0)
turtle.hideturtle()
turtle.speed(0)
turtle.up()

n = 100000
p = (0, 0)
t = turtle.Turtle()
t.up()
t.hideturtle()
for i in range(n):
    t.goto(p)
    t.dot(2, 'green')
    r = random.uniform(0, 1)
    if r < 0.01:
        p = (0, 0.16 * p[1])
    elif r < 0.86:
      p = (0.85 * p[0] + 0.04 * p[1],
      -0.04 * p[0] + 0.85 * p[1] + 1.6)
    elif r < 0.93:
      p = (0.2 * p[0] - 0.26 * p[1],
      0.23 * p[0] + 0.22 * p[1] + 1.6)
    else:
      p = (-0.15 * p[0] + 0.28 * p[1],
      0.26 * p[0] + 0.24 * p[1] + 0.44)

    if i % 1000 == 0:
        t = turtle.Turtle()
        t.up()
        t.hideturtle()
        screen.update()
