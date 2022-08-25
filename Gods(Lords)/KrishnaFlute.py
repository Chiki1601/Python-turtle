import turtle

a = turtle.Turtle()

# steps to start from LEFT side
a.penup()
a.backward(300)
a.right(90)
a.forward(100)
a.pendown()

a.speed(10000)

# ##########         color for FLUTE

a.color("black", "#dcbd9d")
a.begin_fill()

# ################       LEFT CIRCLE
for i in range(360 + 105):
    a.forward(0.50)
    a.left(1)

# #######  BOTTOM LINE
a.forward(500)

# #########  RIGHT CIRCLE
for i in range(360 + 180):
    a.forward(0.50)
    a.left(1)

# ########  TOP LINE
a.forward(500)

# ##########   LEFT CIRCLE OVERLAP
for i in range(275):
    a.forward(0.50)
    a.left(1)

#   TURN POINTER RIGHT SIDE
a.right(100)
a.end_fill()


# #######################       FUNCTION FOR FLUTE INNER HOLE
def inside_hole(o):
    a.color("black")
    a.begin_fill()
    a.penup()
    a.forward(51)
    a.right(90 + o)
    a.pendown()
    for k in range(360 + 180):
        a.forward(0.20)
        a.left(1)
    a.penup()
    a.right(87)
    a.pendown()
    a.end_fill()


# #######     LOOP FOR MAKE 5 HOLES
for i in range(5):

    print(i)
    if i == 2:
        inside_hole(2)
    elif i == 3:
        inside_hole(5)
    else:
        inside_hole(0)

a.penup()
a.forward(74)

a.right(90)

# ##########   RIGHT CIRCLE OVERLAP
for i in range(275):
    a.forward(0.50)
    a.left(1)

a.pendown()
a.right(45)


# #################   FIRST FEATURE   ###################
a.color("black", "#0CA686")
a.begin_fill()
a.forward(15)
a.right(10)
a.forward(20)
a.right(5)
a.forward(30)
a.right(15)
a.forward(20)
a.right(10)
a.forward(20)
a.right(10)
a.forward(25)
a.right(10)
a.forward(20)
a.right(5)
a.forward(50)
a.right(5)
a.forward(70)

a.right(120)

a.right(5)
a.forward(70)
a.right(10)
a.forward(30)
a.right(5)
a.forward(20)
a.right(10)
a.forward(25)
a.right(10)
a.forward(20)
a.right(10)
a.forward(20)
a.right(10)
a.forward(30)
a.right(10)
a.forward(25)
a.right(10)
a.forward(40)
a.end_fill()


# #################   SECOND FEATURE   ###################
a.color("black", "#64DF31")
a.begin_fill()
a.right(90)
a.forward(15)
a.right(15)
a.forward(20)
a.right(10)
a.forward(30)
a.right(10)
a.forward(20)
a.right(10)
a.forward(20)
a.right(10)
a.forward(25)
a.right(5)
a.forward(20)
a.right(5)
a.forward(30)
a.right(5)
a.forward(60)

a.right(120)

a.right(5)
a.forward(70)
a.right(15)
a.forward(30)
a.right(15)
a.forward(30)
a.right(15)
a.forward(20)
a.right(5)
a.forward(25)
a.right(5)
a.forward(20)
a.right(10)
a.forward(52)
a.end_fill()

# #################   THIRD FEATURE   ###################
a.color("black", "#B27F25")
a.begin_fill()
a.right(105)
a.forward(15)
a.right(15)
a.forward(20)
a.right(10)
a.forward(30)
a.right(10)
a.forward(20)
a.right(10)
a.forward(20)
a.right(10)
a.forward(25)
a.right(10)
a.forward(70)

a.right(110)

a.right(10)
a.forward(30)
a.right(10)
a.forward(10)
a.right(10)
a.forward(20)
a.right(10)
a.forward(25)
a.right(10)
a.forward(20)
a.right(10)
a.forward(50)
a.right(15)
a.forward(50)
a.end_fill()


# #################   FOURTH FEATURE   ###################
a.color("black", "#01D1AE")
a.begin_fill()
a.right(125)
a.forward(15)
a.right(10)
a.forward(20)
a.right(5)
a.forward(10)
a.right(5)
a.forward(20)
a.right(5)
a.forward(20)
a.right(5)
a.forward(20)
a.right(10)
a.forward(20)
a.right(10)
a.forward(50)

a.right(110)

a.right(15)
a.forward(20)
a.right(10)
a.forward(10)
a.right(10)
a.forward(20)
a.right(10)
a.forward(25)
a.right(7)
a.forward(40)
a.right(15)
a.forward(20)
a.right(5)
a.forward(20)
a.right(5)
a.forward(20)
a.end_fill()

# #################   FIVE FEATURE   ###################
a.color("black", "#01ACD4")
a.begin_fill()
a.right(140)
a.forward(15)
a.right(5)
a.forward(20)
a.right(5)
a.forward(40)
a.right(10)
a.forward(30)
a.right(10)
a.forward(30)

a.right(130)

a.right(15)
a.forward(20)
a.right(5)
a.forward(10)
a.right(5)
a.forward(20)
a.right(5)
a.forward(25)
a.right(5)
a.forward(20)
a.right(15)
a.forward(45)
a.end_fill()

# #################   SIXTH FEATURE   ###################
a.color("black", "#020556")
a.begin_fill()
a.right(155)
a.forward(40)
a.right(10)
a.forward(20)
a.right(5)
a.forward(10)
a.right(5)
a.forward(10)
a.right(5)
a.forward(10)

a.right(140)

a.forward(10)
a.right(5)
a.forward(10)
a.right(10)
a.forward(20)
a.right(15)
a.forward(20)
a.right(10)
a.forward(20)
a.end_fill()

turtle.done()
