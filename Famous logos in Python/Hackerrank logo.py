#Hackerrank logo in Python

from turtle import *
speed(5)
bgcolor("#100D2B")
pu()
bk(300)
pd()

color("#278343")
pensize(5)
rt(90)
begin_fill()
for i in range(6):
    fd(60)
    rt(60)
end_fill()
color("white")
pu()
lt(90)
bk(85)
pd()
pensize(1)
begin_fill()
lt(45)
fd(20)
rt(90)
fd(20)
rt(135)
fd(6.14)

for i in range(3):
    lt(90)
    fd(20)
rt(90)
fd(16)
rt(90)
fd(56)
lt(90)
fd(6.14)
rt(135)
fd(20)
rt(90)
fd(20)
lt(225)
fd(6.14)

for i in range(3):
    lt(90)
    fd(20)
rt(90)
fd(16)
rt(90)
fd(56)
lt(90)
fd(6.14)
end_fill()
pu()
lt(90)
fd(85)
lt(90)
fd(100)
write("HackerRank",move = False, align= "left", font=("CArial",72,"bold"))
fd(570)
lt(90)
fd(25)
pd()
color("#278343")
begin_fill()
pensize(5)
for i in range(2):
    fd(75)
    rt(90)
    fd(50)
    rt(90)
rt(45)
fd(15)
end_fill()


ht()
done()
