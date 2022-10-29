#awesome design 90
from turtle import *
tracer(10)
pensize(5)
lt(45)
up()
goto(150,0)
down()
for i in range(170):
    color("#FFCC99")
    up()
    circle(170-i,81)
    down()
    rt(1)
    circle(170+i,80)
    
ht()
done()
