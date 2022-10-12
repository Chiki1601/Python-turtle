#cute wallpaper 16
from turtle import *
import colorsys
tracer(624)
bgcolor("black")

def H():
    h = 0
    n = 1445

    for i in range(1000):
        c = colorsys.hsv_to_rgb(h,1,1)
        pencolor(c)
        up()
        goto(0,0)
        down()
        h +=1/n
        pensize(7)
        color("black")
        fd(i)
        circle(i,15)
        for j in range(15):
            c = colorsys.hsv_to_rgb(h,1,1)
            h +=1/n
            pencolor(c)
            circle(j,100)
            
H()           
            
ht()
done()
