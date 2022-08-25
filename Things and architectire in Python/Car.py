#car drawing in Python

import turtle
   
    
PoojasCar = turtle.Turtle()
  
  
# code for drawing rectangular upper body
PoojasCar.color('black')
PoojasCar.fillcolor('red')
PoojasCar.penup()
PoojasCar.goto(0,0)
PoojasCar.pendown()
PoojasCar.begin_fill()
PoojasCar.forward(370)
PoojasCar.left(90)
PoojasCar.forward(50)
PoojasCar.left(90)
PoojasCar.forward(370)
PoojasCar.left(90)
PoojasCar.forward(50)
PoojasCar.end_fill()
   
    
# code for drawing window and roof
PoojasCar.penup()
PoojasCar.goto(100, 50)
PoojasCar.pendown()
PoojasCar.setheading(45)
PoojasCar.forward(70)
PoojasCar.setheading(0)
PoojasCar.forward(100)
PoojasCar.setheading(-45)
PoojasCar.forward(70)
PoojasCar.setheading(90)
PoojasCar.penup()
PoojasCar.goto(200, 50)
PoojasCar.pendown()
PoojasCar.forward(49.50)
   
    
# code for drawing two tyres
PoojasCar.penup()
PoojasCar.goto(100, -10)
PoojasCar.pendown()
PoojasCar.color('black')
PoojasCar.fillcolor('black')
PoojasCar.begin_fill()
PoojasCar.circle(20)
PoojasCar.end_fill()
PoojasCar.penup()
PoojasCar.goto(300, -10)
PoojasCar.pendown()
PoojasCar.color('black')
PoojasCar.fillcolor('black')
PoojasCar.begin_fill()
PoojasCar.circle(20)
PoojasCar.end_fill()
   
    
PoojasCar.hideturtle()

turtle.done()
