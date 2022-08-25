#pizza in Python

#pizza drawing in Python


import turtle

background="#9EC388"
crust="#ECA84F"
sauce="#AD0509"
cheese="#FBC70F"

pepperoni=[[-70,105],[-85,175],[-25,50],[-15,100],[-25,150],[-30,205],[15,50],[20,120],[20,200],[60,156],[71,215],[80,90]]


screen=turtle.Screen()
screen.bgcolor(background)
screen.title("my pizza")

my_turtle=turtle.Turtle()
my_turtle.pensize(5)
my_turtle.shape("circle")

def draw_circle(radius,line_color,fill_color):
    my_turtle.color(line_color)#draw the circle with the defined line color
    my_turtle.fillcolor(fill_color)#fill the circle
    my_turtle.begin_fill()
    my_turtle.circle(radius)
    my_turtle.end_fill()
    
    
def move_turtle(x,y):
    my_turtle.up   #my_turtle.penup()
    my_turtle.goto(x,y) #move the turtle
    my_turtle.down   #my_turtle.pendown()
    
    
draw_circle(150,crust,crust)  #first circle for the crust which is drawn and filled by the same color
move_turtle(0,25)
draw_circle(125, sauce, cheese) #second circle with our sauce color and filled with cheese color

#draw pepperoni
for i in pepperoni:
    my_turtle.penup()
    move_turtle(i[0],i[1])
    draw_circle(10,sauce,sauce)
    
    

move_turtle(0,150)
my_turtle.color(background)

for x in range(0,8):
    my_turtle.pendown()
    my_turtle.left(45)
    my_turtle.forward(150)
    my_turtle.penup()
    my_turtle.backward(150)
    
