from turtle import *
import time

def draw_petal(turtle, radius):
	heading = turtle.heading()
	turtle.shape("turtle")
	turtle.begin_fill()
	turtle.fillcolor("red")
	turtle.circle(radius, 60)
	turtle.left(120)
	turtle.circle(radius, 60)
	turtle.setheading(heading)
	turtle.end_fill()
	
	
	
my_radius = int(input("What is the radius of the flower? "))
my_petals = int(input("How many petals do you want? "))

flower = Turtle()
screen = Screen()
flower.color("pink")
#color("yellow")
colormode(255)
bgcolor(66,103,178)

for _ in range(my_petals):
    draw_petal(flower, my_radius)
    flower.left(360 / my_petals)

flower.right(90)
flower.color("green")	
flower.forward(150)
time.sleep(3)
flower.reset()
flower.hideturtle()
pen1 = Pen()
pen2 = Pen()
pen1.color("orange")
pen1.write("Happy Rose Day", False , 'center',font=("Monotype Corsiva", 30, "bold"))
time.sleep(3)
pen1.clear()
flower.hideturtle()
pen2.color("red")
pen2.write("By Pooja Patel", False , 'center',font=("Monotype Corsiva", 30, "bold"))
time.sleep(3)
pen2.clear()
screen.bgpic("yt-header.gif")	
flower.hideturtle()


screen.exitonclick()
