#bootstrap logo in Pytohn
from turtle import *

bgcolor('white')
pencolor('Indigo')
width(23)
penup()
goto(160,-90)
pendown()

left(90)
begin_fill()
color("Indigo")
for i in range(4):
 forward(230)
 circle(34,90)
pu()
goto(20,-110)
pd()
end_fill()
color("white")  
write("B", move = False, align = "Center", font= ("Helvetica",170,"bold"))
done()
