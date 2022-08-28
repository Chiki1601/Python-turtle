#flag of Italia


from turtle import *
setup(720,1080)
speed(5)
pu()
goto(-150,150)
pd()
color("black","green")
begin_fill()
for i in range(2):
    fd(100)
    rt(90)
    fd(300)
    rt(90)
end_fill()

fd(200)
color("black","red")
begin_fill()
for i in range(2):
    fd(100)
    rt(90)
    fd(300)
    rt(90)
end_fill()

rt(90)
fd(300)
lt(90)
backward(100)

pu()
goto(-50,160)
rt(154)
color("black")

write("Flag of Italia",font=("Arial",20,"normal"))
pu()
goto(800,0)
done()
