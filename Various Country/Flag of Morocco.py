#flag of Morocco

from turtle import *
setup(720,1080)
speed(5)
pu()
goto(-300,150)
pd()

color("dark red")
begin_fill()
for i in range(2):
    fd(600)
    rt(90)
    fd(400)
    rt(90)
end_fill()

width(13)
pu()
goto(-150,0)
pd()

color("#006233")
for i in range(5):
    fd(300)
    rt(144)
    
pu()
goto(-80,200)
color("#000000")
write("Flag of Morocco",font=("Arial",20,"normal"))
pu()
goto(800,0)
done()
