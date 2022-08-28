#flag of france

from turtle import *
setup(500,500)
speed(0)
title("Flag of France by Pooja Patel")

pu()
goto(-150,50)
pd()

def Rectangle():
    for i in range(2):
        fd(100)
        rt(90)
        fd(200)
        rt(90)
color("blue")       
begin_fill()
Rectangle()
end_fill()
pu()

fd(200)
pd()

color("red")       
begin_fill()
Rectangle()
end_fill()

pu()
goto(-150,50)
color("black")
pd()

for i in range(2):
    fd(300)
    rt(90)
    fd(200)
    rt(90)
pu()
goto(20,70)
write("Flag of France", font=("Arial", 22, "bold"))
pd()
done()
