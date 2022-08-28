import turtle
import math
import random

screen = turtle.Screen()
screen.setup(1000,1000)
screen.title("Random Mountain Curves - PythonTurtle.Academy")

turtle.hideturtle()
turtle.speed(0)
turtle.pensize(2)
turtle.color('dark green')
MAX_SLOPE = 45
MIN_SLOPE = -45
MIN_HEIGHT = 0
def dist_squared(P1,P2):
    return (P1[0]-P2[0])**2 + (P1[1]-P2[1])**2

def mountain(P1,P2):
    if dist_squared(P1,P2) < 9:
        turtle.goto(P2)
        return
    x1,y1 = P1
    x2,y2 = P2
    x3 = random.uniform(x1,x2)
    y3_max = min((x3-x1)*math.tan(math.radians(MAX_SLOPE)) + y1, (x2-x3)*math.tan(-math.radians(MIN_SLOPE)) + y2)
    y3_min = max((x3-x1)*math.tan(math.radians(MIN_SLOPE)) + y1, (x2-x3)*math.tan(-math.radians(MAX_SLOPE)) + y2)
    y3_min = max(y3_min, MIN_HEIGHT)
    y3 = random.uniform(y3_min,y3_max)
    P3 = (x3, y3)
    mountain(P1,P3)
    mountain(P3,P2)
    return

turtle.up()

turtle.goto(-400,MIN_HEIGHT)
turtle.down()
mountain((-400,MIN_HEIGHT),(400,MIN_HEIGHT))
