#awesome design 83


from turtle import *
import colorsys
speed(0)
bgcolor("black")
h = 0.3
pensize(2)
def design(ang,n):
    circle(60+n,90)
    left(ang)
    circle(60+n,90)
up()
goto(0,90)
down()
for i in range(70):
    col = colorsys.hsv_to_rgb(h,0.8,1)
    h += 1/80
    color(col)
    design(120,i)
    design(90,i)
    design(240,i)
    design(90,i)
    design(120,i)
ht()
ht()
done()
