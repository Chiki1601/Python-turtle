#vlc logo in Python
from turtle import*
speed(4)
width()
bgcolor('#D9F1FF')
penup()
goto(-110,-100)
pendown()
color('#E85E00')
begin_fill()
fd(230)
circle(20,106)
fd(80)
circle(25,74)
fd(172)
circle(25,74)
fd(80)
circle(20,106)
end_fill()
penup()
goto(-70,-20)
pendown()
color('white')
begin_fill()
rt(40)
circle(120,80)
lt(69)
fd(50)
lt(111)
circle(-95,80)
lt(111)
fd(50)
end_fill()


rt(180)
fd(50)
color('#E85E00')
begin_fill()
fd(50)
rt(111)
circle(70,80)
rt(111)
fd(50)
rt(69)
circle(-95,80)
end_fill()

rt(69)
fd(50)
color('white')
begin_fill()
fd(50)
rt(111)
circle(44,80)
rt(111)
fd(50)
rt(69)
circle(-70,80)
end_fill()
rt(69)
fd(50)
color('#E85E00')
begin_fill()
fd(30)
circle(-20,142)
fd(30)
rt(69)
circle(-44,80)
end_fill()
hideturtle()
done()
