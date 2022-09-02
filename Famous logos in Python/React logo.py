#react Logo in Python
from turtle import *
speed(5)
bgcolor("black")
pencolor("cyan")
shape("circle")
fillcolor("")
shapesize(15,5,10)
seth(90)

for i in [1,-1]:
    stamp()
    seth(i * 150)
    
dot(50, "cyan")
done()
