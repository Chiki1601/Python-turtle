#adobe Premiere logo in Python
from turtle import *
speed(0)
pu()
goto(-100,-200)
pd()
color("#3C327B")
begin_fill()
for i in range(4):
    fd(200)
    circle(100,90)
end_fill()

pu()
goto(15,-155)
pd()
lt(45)
pu()
goto(-85,-90)
pd()
color("#88C3FC")
write("Pr",font=("Calibri (Body)",120,"bold"))

ht()
done()
