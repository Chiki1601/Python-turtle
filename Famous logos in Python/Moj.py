#moj logo in Python

import turtle as t
t.speed(2)
t.width(2)
def realtive_pos(x,y):
    
    t.penup()
    t.goto(t.pos()+(x,y))
    t.pendown()
t.begin_fill()
t.color("#ffab00")
for i in range(4):
    t.fd(100)
    t.circle(100,90)
t.end_fill()
realtive_pos(140,70)

t.seth(90)
t.color("#000")
t.begin_fill()

for i in range(3):
    if(i==1):
        t.forward(169.71)
    else:
        t.fd(120)
    t.circle(10,135)
   
t.end_fill()
realtive_pos(-180,40)
            
t.seth(90)
t.width(20)
for i in range(4):
    t.fd(60)
    if i==1:
        t.left(90)
        
    else:
        t.right(90)
t.hideturtle()
t.done()
