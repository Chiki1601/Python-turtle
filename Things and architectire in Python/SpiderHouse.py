#spyder house using python
import turtle as t
# define turtle speed
t.speed(2)

# radical thread
for i in range(6):
	t.forward(100)
	t.backward(100)
	t.right(60)

# spiral thread length
side = 50

# Spider web color
t.fillcolor("Yellow")

# building web
t.begin_fill()

for i in range(10):
	t.penup()
	t.goto(0, 0)
	t.pendown()
	t.setheading(0)
	t.forward(side)
	t.right(120)
	for j in range(6):
		t.forward(side-2)
		t.right(60)
	side = side - 10

t.end_fill()
