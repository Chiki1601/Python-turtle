#adobe loghtroom logo in Python
from turtle import *
speed(0)
pu()
goto(-100,-200)
pd()
color("#002059")
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
goto(-150,-160)
pd()
color("#3BCEE5")
write("Lr",font=("Calibri (Body)",230,"bold"))

ht()
done()
