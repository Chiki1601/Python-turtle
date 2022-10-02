import math
import turtle

tina = turtle.Turtle()
tina.shape("turtle")
tina.color("black")
tina.speed(0)

def pos(x,y):
tina.penup()
tina.goto(x,y)
tina.pendown()
tina.color("red")
tina.begin_fill()
pos(0,-250)

tina.circle(250)


tina.end_fill()


def draw(t, numseeds, angle, cspread):
    t.fillcolor("orange")
    phi = angle * (math.pi / 120.0)
   
    for i in range (numseeds):
      # figure out the next x, y position
      r = cspread * math.sqrt(i)
      theta = i * phi
      x = r * math.cos(theta)
      y = r * math.sin(theta)

      # move the turtle and orient it correctly
      t.penup()
      t.goto(x, y)
      t.setheading(i * angle)

      if i <  numseeds:
        t.stamp()
      

draw(tina,500,18.7,9)   

pos(250,0)
tina.pensize(15)
tina.pencolor("gold")
for i in range(40):
tina.left(5)
tina.forward(25)

pos(-250,0)
tina.pensize(15)
tina.pencolor("gold")
for i in range(40):
tina.left(5)
tina.forward(25)
