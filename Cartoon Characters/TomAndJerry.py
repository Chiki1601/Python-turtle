#Babyshark drawing in Python turtle



import turtle as t 
t.speed(0)

t.width(2)
color = "#ffd202"

def relative_Pos(x,y):
    t.penup()
    t.goto(t.pos()+(x,y))
    t.pendown()
    
def fillCircle(col,fcol,r):
    t.begin_fill()
    t.color(col)
    t.fillcolor(fcol)
    t.circle(r)
    t.end_fill()
    
def BabyShark():
    t.seth(-90)
    t.circle(80,180)
    t.begin_fill()
    t.circle(64,70)
    t.fd(80/3)
    t.rt(45)
    t.fd(80/3)
    t.lt(135)
    t.fd(80/3)
    t.rt(55)
    t.fd(80/3)
    t.circle(64,75)
    t.seth(0)
    t.circle(-80,30)
    t.circle(80,30)
    t.circle(80,30)
    t.circle(-80,30)
    t.fillcolor(color)
    t.end_fill()
    
    relative_Pos(-75,0)
    fillCircle("black","#b47a22",3)
    relative_Pos(-10,0)
    fillCircle("black","#b47a22",3)
    relative_Pos(-20,0) 
    t.circle(15)
    relative_Pos(2,3)
    fillCircle("black","black",10)
    relative_Pos(-5,15)
    fillCircle("white","white",2)
    relative_Pos(60,-15)
    t.color("black")
    t.circle(15)
    relative_Pos(2,3)
    fillCircle("black","black",10)
    relative_Pos(-7,10)
    fillCircle("white","white",2)
    relative_Pos(15,-25)
    t.seth(-90)
    t.color("black")
    t.begin_fill()
    t.fillcolor("#9d0f3b")
    t.circle(-40,175)
    t.seth(-20)
    t.circle(80,5)
    for j in range(2):
        for i in range(3):
            t.circle(80,2)
            t.rt(60)
            t.fd(8)
            t.lt(120)
            t.fd(7+j)
            t.rt(60)
        if j == 0 :
            t.seth(10)
    t.circle(80,8)
    t.end_fill()
    relative_Pos(-17,-28)
    t.seth(135)
    t.begin_fill()
    t.fillcolor("#db4141")
    t.circle(30,92)
    t.seth(-45)
    t.circle(30,92)
    t.end_fill()
    relative_Pos(45,0)
    t.seth(-10)
    t.begin_fill()
    t.fillcolor(color)
    t.circle(-80,40)
    t.rt(90)
    t.circle(-80,40)
    t.left(80)
    t.fd(20)
    t.circle(40,90)
    t.lt(60)
    t.circle(-70,40)
    t.rt(150)
    t.circle(80,60)
    t.rt(145)
    t.circle(-70,30)
    t.seth(-165)
    t.circle(-120,90)
    t.left(90)
    t.circle(-80,40)
    t.rt(90)
    t.circle(-80,45)
    t.seth(-60)
    t.circle(70,30)
    t.rt(60)
    t.circle(100,110)
    t.lt(145)
    t.circle(-60,90)
    t.fd(35)
    t.rt(30)
    t.circle(30,30)
    t.end_fill()
    
relative_Pos(-220,100)
BabyShark()
relative_Pos(80,180)
color = "#f229d4"
BabyShark()
relative_Pos(-100,-300)
color = "#0361a2"
BabyShark()
t.hideturtle()
t.done()