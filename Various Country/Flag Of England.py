#flag Of England
from turtle import *

speed(3)
bgcolor('grey')
hideturtle()

color('white')
begin_fill()
fd(225)
lt(90)
fd(165)
lt(90)
fd(225)
lt(90)
fd(165)
lt(90)
lt(90)
fd(70)
rt(90)
end_fill()

color('red')
begin_fill()
fd(100)
rt(90)
fd(70)
lt(90)
fd(25)
lt(90)
fd(70)
rt(90)
fd(100)
lt(90)
fd(25)
lt(90)
fd(100)
rt(90)
fd(70)
lt(90)
fd(25)
lt(90)
fd(70)
rt(90)
fd(100)
lt(90)
fd(30)
end_fill()

color('black')
begin_fill()
lt(180)
fd(108)
lt(90)
fd(7)
lt(90)
fd(450)
lt(90)
fd(7)
lt(90)
fd(450)
end_fill()

penup()
lt(180)
fd(300)
lt(90)
fd(50)
pendown()
color('white')
write('England Flag',font=('arial',20,'normal'))

done()
