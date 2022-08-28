#flag of Russia
import turtle

x = turtle.Screen()
x.bgcolor("#b940ff")
x.title("The Russian Flag")

pp = turtle.Turtle()

pp.shape("turtle")

pp.up()
pp.goto(-350, 300)
pp.down()

for i in range(2):
    pp.fd(150)
    pp.rt(90)
    pp.fd(90)
    pp.rt(90)

pp.color("white")
pp.speed(20)

for i in range(15):
    pp.fd(150)
    pp.rt(90)
    pp.fd(1)
    pp.rt(90)
    pp.fd(150)
    pp.lt(90)
    pp.fd(1)
    pp.lt(90)

pp.color("blue")
for i in range(15):
    pp.fd(150)
    pp.rt(90)
    pp.fd(1)
    pp.rt(90)
    pp.fd(150)
    pp.lt(90)
    pp.fd(1)
    pp.lt(90)

pp.color("red")
for i in range(15):
    pp.fd(150)
    pp.rt(90)
    pp.fd(1)
    pp.rt(90)
    pp.fd(150)
    pp.lt(90)
    pp.fd(1)
    pp.lt(90)

pp.fd(150)

turtle.done()
