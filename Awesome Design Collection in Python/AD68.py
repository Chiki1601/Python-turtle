# Awesome Design 68

from turtle import *
import random

for n in range(60):
    speed(0)
    penup()
    goto(random.randint(-400, 400), random.randint(-400, 400))
    pendown()

    red_amount   = random.randint( 0,  30) / 100.0
    red_amount  = random.randint(50, 100) / 100.0
    green_amount = random.randint( 0,  30) / 100.0
    pencolor((red_amount, green_amount, red_amount))

    circle_size = random.randint(10, 40)
    pensize(random.randint(1, 5))

    for i in range(6):
        circle(circle_size)
        left(60)

done()
