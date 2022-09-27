#sunflower drawing in Python
from turtle import *
import colorsys
speed(0)
bgcolor("black")
h = 0.1
up()
goto(100,50)
down()

for i in range(50):
    c= colorsys.hsv_to_rgb(h,1,1)
    color(c)
    begin_fill()
    for j in range(2):
        rt(99)
        circle(150,-100)
    rt(10)
    lt(90)
    h += 0.001
    end_fill()
ht()
done()
