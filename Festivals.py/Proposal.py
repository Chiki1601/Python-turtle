import turtle

print("                            ############🤩LOVES ME OR NOT🙁################\n")
print("                                                -create by Pooja Patel")
smp='yes'
smp2='no'
girl_name=input("Enter the name:\n\t")
ram=(input("Do you Like me "+girl_name+" , just say yes or no:\n\t"))
if (ram==smp!=smp2):
    pen = turtle.Turtle()
    def curve():
        for i in range(200):
            pen.right(1)
            pen.forward(1)
    def heart():
        pen.speed(420)
        pen.fillcolor('red')
        pen.begin_fill()
        pen.left(140)
        pen.speed(190)
        pen.forward(113)
        curve()
        pen.left(120)
        curve()
        pen.forward(112)
        pen.end_fill()
    def text():
        pen.up()
        pen.setpos(-120,-50)
        pen.down()
        pen.color('#00999c')
        pen.write("😘😍I Love You "+girl_name, font=("verdana", 21, "bold"))
    heart()
    text()
    pen.ht()
    turtle.done()

elif(ram==smp2!=smp):

    pen = turtle.Turtle()
    def curve():
        for i in range(200):
            pen.right(1)
            pen.forward(1)
    def heart():
        pen.speed(420)
        pen.fillcolor('red')
        pen.begin_fill()
        pen.left(140)
        pen.speed(190)
        pen.forward(113)
        curve()
        pen.left(120)
        curve()
        pen.forward(112)
        pen.end_fill()
        # turtle.done()
    heart()
    pen.penup()
    pen.goto(0, 160)
    pen.pendown()
    for i in range(3):
        pen.color("white")
        pen.width(3.9)
        pen.left(75)
        pen.forward(40)
        pen.right(65)
        pen.forward(40)
    pen.ht
    def txt():
        pen.penup()
        pen.setpos(-120, -50)
        pen.pendown()
        pen.color("#00999c")
        pen.write("🥺💔you broke me "+girl_name, font=("verdana", 21, "bold"))
    txt()
    pen.ht()
    turtle.done()

else:
    print("😵‍💫invalid statement,just say yes/no😉")
