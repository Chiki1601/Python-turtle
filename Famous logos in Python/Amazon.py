#Amazon logo in Pytohn turtle

from turtle import *
ht()
x = ("Calibry",30,"bold")
write("amazon",font = x)
up()
goto(20,5)
down()
color("orange")
rt(35)



for x,y in zip(
    [3,4,5,4,3],[10,10,30,10,10]
):
    width(x)
    circle(50,y)
    
up()
goto(73,9)
down()
rt(32)
fd(8)
rt(100)
fd(8)
done()
