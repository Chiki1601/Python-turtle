#tri color wallpaper 2
from turtle import *
import random
bgcolor("black")
tracer(1000)
pensize(1)
def design(x,y,col):
    up()
    goto(x,y)
    down()
    color(col)
    for i in range(50):
        circle(i,181)
        rt(1)
        circle(50-i,91)
        
for i in range(30):
    design((random.randint(-350,350)),(random.randint(-700,700)),"orange")
    design((random.randint(-350,350)),(random.randint(-700,700)),"white")
    design((random.randint(-350,350)),(random.randint(-700,700)),"green")

ht()
done()
