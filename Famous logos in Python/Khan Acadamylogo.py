#khan acadamy logo in Python
import turtle as t
from turtle import Screen, Turtle

RADIUS = 100

screen = Screen()
screen.colormode(255)

turtle = Turtle(visible=False)
turtle.speed('fastest')  # because I have no patience
turtle.penup()  # we'll use fill instead of lines
turtle.color(20, 191, 150)  # greenish color

turtle.sety(-RADIUS)  # center hexagon
turtle.begin_fill()
turtle.circle(RADIUS, steps=6)  # draw hexagon
turtle.end_fill()

turtle.color('white')  # interior color
turtle.sety(2 * RADIUS / 11)  # position circle (head)
turtle.begin_fill()
turtle.circle(2 * RADIUS / 9)  # draw circle (head)
turtle.end_fill()

turtle.forward(5 * RADIUS / 8)
turtle.right(85)

turtle.begin_fill()
turtle.circle(-13 * RADIUS / 20, 190)
turtle.right(85)
turtle.circle(-13 * RADIUS / 20, 90)
turtle.left(180)
turtle.circle(-13 * RADIUS / 20, 90)
turtle.end_fill()

screen.exitonclick()
