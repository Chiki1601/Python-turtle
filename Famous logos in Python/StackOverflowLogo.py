#stack overflow logo in Python

from turtle import *
pu()
speed(5)
bk(350)
pd()
color("#808080")
pensize(20)
rt(90)
fd(100)
lt(90)
fd(250)
lt(90)
fd(100)
bk(20)
color("orange")
pensize(4)
lt(90)
pu()
fd(25)
pd()
for x in range(5):
    for y in range(2):
        begin_fill()
        fd(200)
        lt(90)
        fd(25)
        lt(90)
        end_fill()
    rt(90)
    pu()
    fd(40)
    pd()
    lt(75)
    
lt(75)
rt(90)
pu()
bk(350)
pd()
color("black")
write("overflow",move = False, align= "left", font=("Century gothic",72,"bold"))
write("stack",move = False, align= "right", font=("Century gothic",72,"normal"))
ht()
done()