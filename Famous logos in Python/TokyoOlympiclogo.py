import turtle as t


t.speed(5)
t.width(10)
t.penup()
t.goto(-170,-100)
t.pendown()
x=-170

tokyo = ["blue","black","red"] ## take the variable for selecting color called tokyo
for i in tokyo:
    t.color(i)## color items
    t.circle(80)
    t.penup()
    t.goto(x+195,-100)
    x=x+195
    t.pendown()

t.penup()
t.goto(-70,-170)
t.pendown()

t.color("yellow")
t.circle(80)

t.penup()
t.goto(130,-170)
t.pendown()

t.color("green")
t.circle(80)

t.penup()
t.goto(-220,170)
t.pendown()

t.color("blue")
t.write("TOKYO OLYMPIC",font=("helvetica",40))

t.hideturtle()
t.done()    
