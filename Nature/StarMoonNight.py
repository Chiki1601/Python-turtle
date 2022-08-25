import turtle as t
import random

SCREEN_WIDTH=1000
SCREEN_HEIGHT=1000
STAR_COLOR="#f0ffff"
MOON_COLOR="#FFFFF0"
NIGHT_COLOR="black"

t.Screen().tracer(0,0)
t.Screen().screensize(SCREEN_WIDTH,SCREEN_HEIGHT)
t.Screen().setworldcoordinates(-SCREEN_WIDTH,-SCREEN_HEIGHT,SCREEN_WIDTH,SCREEN_HEIGHT)
t.Screen().bgcolor(NIGHT_COLOR)

def moon(size=100):
  t.penup()
  t.left(20)

  t.color(MOON_COLOR, MOON_COLOR)
  t.dot(size)
  t.forward(size*.25)
  t.color(NIGHT_COLOR, NIGHT_COLOR)
  t.dot(size)

def random_star():
  t.penup()
  t.color(STAR_COLOR, STAR_COLOR)

  x=random.randint(-SCREEN_WIDTH,SCREEN_WIDTH)
  y=random.randint(-SCREEN_HEIGHT,SCREEN_HEIGHT)

  dot_size=random.random()*3

  t.goto(x,y)
  t.dot(dot_size)


for _ in range(1000):
    random_star()

moon(150)

t.hideturtle()
t.Screen().update()
t.done()
