import turtle as t

t.bgcolor("gold")
def pos(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
#For Tika
pos(0,200)
t.color("black")
t.begin_fill()
t.circle(40)
t.end_fill()

#For Left Eyebrow
pos(-30,200)
t.begin_fill()
t.right(45)
for i in range(20):
    t.left(3)
    t.back(10)
for i in range(10):
    t.right(3)
    t.back(10)
t.right(18)
for i in range(13):
    t.left(3)
    t.forward(10)
for i in range(20):
    t.right(2)
    t.forward(10)
t.end_fill()


#For Right Eyebrow
t.left(80)
pos(30,200)
t.begin_fill()
for i in range(20):
    t.right(3)
    t.forward(10)
for i in range(10):
    t.left(3)
    t.forward(10)
t.left(18)
for i in range(13):
    t.right(3)
    t.back(10)
for i in range(20):
    t.left(2)
    t.back(10)
t.end_fill()

#For Right Eye
pos(40,150)
t.pensize(15)
t.left(10)
for i in range(20):
    t.right(3)
    t.forward(10)
for i in range(10):
    t.left(3)
    t.forward(5)
t.right(3)
for i in range(10):
    t.left(3)
    t.back(5)
for i in range(20):
    t.right(3)
    t.back(10)
t.pensize(1)
pos(130,130)
t.begin_fill()
t.circle(40)
t.end_fill()
t.color("white")
t.begin_fill()
pos(115,175)
t.circle(10)
t.end_fill()


#For Right Eye
pos(-40,150)
t.color("black")
t.pensize(15)
t.right(25)
for i in range(20):
    t.left(3)
    t.back(10)
for i in range(10):
    t.right(3)
    t.back(5)
t.left(3)
for i in range(10):
    t.right(3)
    t.forward(5)
for i in range(20):
    t.left(3)
    t.forward(10)
t.pensize(1)
pos(-130,130)
t.begin_fill()
t.circle(40)
t.end_fill()
t.color("white")
t.begin_fill()
pos(-155,175)
t.circle(10)
t.end_fill()

#For Nose
t.color("black")
pos(-60,10)
t.right(70)
for i in range(5,12):
    t.pensize(i)
    t.left(7)
    t.forward(10)
for i in range(12,5,-1):
    t.pensize(i)
    t.left(7)
    t.forward(10)

#for lip
t.begin_fill()
pos(-130,-90)
t.pensize(1)
t.begin_fill()
t.right(60)
for i in range(3):
    t.left(3)
    t.forward(5)
for i in range(10):
    t.left(4)
    t.forward(6)
for i in range(10):
    t.right(10)
    t.forward(7)
t.left(135)
for i in range(10):
    t.right(10)
    t.forward(7)
t.right(2)
for i in range(10):
    t.left(4)
    t.forward(6)
for i in range(3):
    t.left(3)
    t.forward(5)

t.right(160)
for i in range(12):
    t.right(3)
    t.forward(7.2)
t.left(44)
for i in range(15):
    t.right(5.5)
    t.forward(7)
t.left(44)
for i in range(12):
    t.right(3)
    t.forward(7)
t.end_fill()
#For lower Lip
t.begin_fill()
t.left(175)
for i in range(14):
    t.left(2)
    t.forward(5)
t.right(45)
for i in range(14):
    t.left(7)
    t.forward(10)
t.right(45)
for i in range(14):
    t.left(3)
    t.forward(5)
t.right(185)
for i in range(7):
    t.left(3)
    t.forward(10)
t.right(.6)
for i in range(18):
    t.right(6)
    t.forward(10)
t.right(8)
for i in range(7):
    t.left(3)
    t.forward(10)
t.end_fill()
#For Nosering
t.pensize(12)
t.color("red")
pos(30,0)
t.left(120)
for i in range(47):
    t.right(7)
    t.back(10)
t.hideturtle()
t.exitonclick()
