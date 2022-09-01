#flash logo in Python

import turtle

turtle.bgcolor("darkred")
turtle.speed(5)

turtle.penup()
turtle.goto(-90,-150)
turtle.pendown()

turtle.pensize(20)
turtle.pencolor("yellow")
turtle.circle(200)

turtle.penup()
turtle.fd(200)
turtle.lt(90)
turtle.fd(500)
turtle.rt(45)
turtle.pendown()

turtle.fillcolor("#fdc04e")
turtle.begin_fill()
turtle.pensize(2)
turtle.backward(350)
turtle.rt(45)
turtle.fd(80)
turtle.rt(-45)
turtle.backward(200)
turtle.rt(45)
turtle.fd(80)
turtle.rt(-45)
turtle.backward(300)
turtle.rt(5)
turtle.fd(450)
turtle.rt(37)
turtle.backward(80)
turtle.lt(45)
turtle.fd(170)
turtle.rt(45)
turtle.backward(60)
turtle.lt(54)
turtle.fd(235)
turtle.end_fill()


turtle.mainloop()
