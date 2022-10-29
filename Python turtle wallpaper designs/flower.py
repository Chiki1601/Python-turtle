#flower wallpaper design in Python
from turtle import *
import random
bgcolor("black")
tracer(100)
pensize(2)

r = random.randint(0,255)
g = random.randint(0,255)
b = random.randint(0,255)
colormode(255)
def design(x,y):
    up()
    goto(x,y)
    down()
    color(r,g,b)
    for j in range(20):
        up()
        fd(j)
        rt(91)
        down()
        circle(j)
for i in range(300):
    design(random.randint(-350,350),(random.randint(-700,700)))
    
ht()
done()
