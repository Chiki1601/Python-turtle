import turtle

t = turtle.Turtle()
t.left(90)
t.speed(100)

def tree(i):
	if i < 10:
		return
	else:
		t.forward(i)
		t.left(30)
		t.color("red")
		tree(3*i/4)
		t.right(60)
		t.color("green")
		tree(3*i/4)
		t.left(30)
		t.backward(i)


tree(100)

def setPosition(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    
setPosition(-80, -200)
t.color("green")
t.write("Save Tree, Save Life.... ", 
font=("Calibri", 25, "bold")
)

turtle.done()
