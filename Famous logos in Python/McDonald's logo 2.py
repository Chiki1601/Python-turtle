#McDonald's logo 2 in Python

from turtle import *
write("McDonald's logo 2 by Pooja Patel")
speed(1)
bgcolor("red")
pen(pencolor="yellow")
shape("circle")
fillcolor("")
shapesize(20,5,20)
penup()

for i in [1,2]:
    bk(50*i) if i%2!=0 else fd(50*i)
    stamp()
shape("square")
pen(pencolor="red")
fillcolor("red")
shapesize(18,18,0)
goto(0,-180)
done()
