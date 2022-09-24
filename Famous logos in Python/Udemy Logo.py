#Udedmy logo in Python

from turtle import *
import time

pu()
goto(-100,-200)
pd()
time.sleep(0.3)
write("U",font=("Times Now",250,"normal"))
pu()
fd(26)
rt(90)
bk(350)
pd()
time.sleep(0.5)
pencolor("#a35ecb")
fillcolor("#a35ecb")
begin_fill()
bk(40)
rt(60)
bk(107)
rt(60)
bk(107)
rt(60)
bk(40)
rt(120)
bk(107)
rt(120)
fd(107)
end_fill()

ht()
done()
