# Ice ceram wallpaer art in Python
from turtle import *
import random
bgcolor("black")
for i in range(80):
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    colormode(255)
    color(r,g,b)
    begin_fill()
    up()
    goto(random.randint(-400,400),random.randint(-800,800))
    down()
    write("🍧🍦🧁",font=("Calibri",random.randint(5,22),"bold"))
    end_fill()
ht()
done()
