#meesho logo in Python
from turtle import *

bgcolor('white')
pencolor('hot pink')
width(23)
penup()
goto(160,-90)
pendown()

left(90)
begin_fill()
color("deep pink")
for i in range(4):
 forward(230)
 circle(34,90)
pu()
goto(-150,-10)
pd()
end_fill()
color("white")    
write("meesho", move = False, font= ("Century Gothic",62,"bold"))



done()
