#google photos logo in Python
import turtle
pooja = turtle.Screen()
pen = turtle.Turtle()
pooja.setup(700,1000,0,0)
pen.speed(5)
pen.width(3)
for i in range(1):
    for colors in ("blue","red","yellow","green"):
        pen.begin_fill()
        pen.color(colors)
        pen.fd(300)
        pen.rt(90)
        pen.circle(-150,180)
        pen.end_fill()
        pen.fillcolor(colors)
        
pen.up()
pen.rt(80)
pen.fd(300)
#write your name
pen.color("black")
pen.write("By Pooja Patel",font=("Times New Roman",35,"bold"))
pen.hideturtle()
turtle.done()
