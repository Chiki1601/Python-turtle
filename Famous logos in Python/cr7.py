#CR7 logo in Python
import turtle

turtle.bgcolor('black')
pp = turtle.Turtle()
pp.pencolor('white')
pp.hideturtle()

pp.penup()
pp.goto(-250, 100)
pp.pendown()

pp.color('white')
pp.begin_fill()
pp.fd(50)

pp.lt(110)

for i in range(31):
    pp.lt(10)
    pp.fd(25)

pp.lt(120)
pp.fd(50)

pp.lt(58)

for i in range(26):
    pp.rt(11)
    pp.fd(19.3)

pp.end_fill()

pp.penup()
pp.goto(-150, 183)
pp.pendown()
pp.begin_fill()
pp.rt(42)
pp.fd(287)

pp.lt(90)
pp.fd(50)

pp.lt(90)
pp.fd(250)

pp.rt(90)
pp.fd(90)

for i in range(60):
    pp.rt(3)
    pp.fd(3)

pp.fd(85)

pp.lt(130)
pp.fd(180)

pp.lt(50)
pp.fd(55)

pp.lt(130)
pp.fd(134)

pp.rt(130)
pp.fd(17)


for i in range(60):
    pp.lt(3)
    pp.fd(4.9)


pp.fd(150)
pp.end_fill()

pp.penup()
pp.goto(150, 183)
pp.pendown()
pp.begin_fill()

pp.lt(60)
pp.fd(50)

pp.lt(120)
pp.fd(150)

pp.rt(120)
pp.fd(500)

pp.lt(175)
pp.fd(580)

pp.lt(125)
pp.fd(210)
pp.end_fill()

pp.penup()
pp.goto(170, 210)
pp.pendown()
pp.begin_fill()

pp.rt(120)
pp.fd(200)

pp.rt(170)
pp.fd(185)

pp.rt(70)
pp.fd(40)
pp.end_fill()

pp.penup()
pp.goto(170, 210)
pp.pendown()

turtle.mainloop()
