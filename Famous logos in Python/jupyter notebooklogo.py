#jupyter notebook logo in Python
from turtle import *
tracer(10)
pensize(5)
lt(45)
up()
goto(150,0)
down()
for i in range(90):
    color("#FFCC99")
    up()
    circle(170-i,91)
    down()
    rt(1)
    circle(170+i,90)

ht()
done()
