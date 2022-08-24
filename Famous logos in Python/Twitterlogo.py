#twitter logo in Python
from turtle import *
speed(1000)
fillcolor('#1DA1F2')
begin_fill()
penup()
goto(50,80)
left(100)
pendown()
# head start
for i in range(150):
    forward(0.8)
    right(1)
left(70)
# head end
# leaps start
for i in range(55):
    forward(0.5)
    left(0.5)
right(135)
for i in range(55):
    forward(0.5)
    right(1)
left(160)
forward(20)
right(135)
for i in range(55):
    forward(0.5)
    right(0.5)
# leaps end
# lower part
left(50)
for i in range(90):
    forward(2.5)
    right(1)
for i in range(40):
    forward(1)
    right(0.3)
# end of lower part
right(160)
for i in range(63):
    forward(1)
    left(0.5)
left(160)
for i in range(90):
    forward(0.5)
    right(1)
right(110)
forward(17)
left(160)
for i in range(100):
    forward(0.5)
    right(0.5)
right(130)
for i in range(50):
    forward(0.5)
    left(0.5)
left(150)
for i in range(150):
    forward(0.5)
    right(0.5)
right(130)
for i in range(100):
    forward(0.5)
    left(0.5)
for i in range(102):
    forward(0.5)
    left(0.1)
end_fill()
hideturtle()
done()
