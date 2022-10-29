#awesome design 115 in Pytohn

from turtle import *
import colorsys
bgcolor("black")
h = 0
speed(0)
shape("circle")
pencolor("blue")
pensize(4)
up()
goto(0,0)
down()
for i in range(800):
    c = colorsys.hsv_to_rgb(h,0.8,1)
    pencolor(c)
    circle(i,100)
    rt(91)
    circle(i,-100)
    h += 0.05
    
ht()
done()
