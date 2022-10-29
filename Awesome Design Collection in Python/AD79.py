#awesome design 79 in Python
from turtle import *
import colorsys
bgcolor("black")
h = 0
speed(0)
def pooja(angle,n):
    circle(20+n,90)
    left(angle)
    circle(20+n,90)
    
goto(0,0)
for i in range(600):
    col = colorsys.hsv_to_rgb(h,0.8,1)
    pencolor(col)
    if i %13 ==0:
        h +=0.05
    pooja(90,i)
    pooja(120,i)
    
ht()
done()
