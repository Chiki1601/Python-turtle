import turtle
screen = turtle.Screen()
screen.setup(800,600)
circle = turtle.Turtle()
circle.shape('circle')
circle.color('#D2042D')
circle.speed('fastest')
circle.up()
square = turtle.Turtle()
square.shape('square')
square.color('#006400')
square.speed('fastest')
square.up()
circle.goto(0,280)
circle.stamp()
r = 0
for i in range(1, 17):
    q = 30*i
    for j in range(i-r):
        p = 30*j
        square.goto(p,-q+280)
        square.stamp()
        square.goto(-p,-q+280)
        square.stamp()
    if i % 4 == 0:
        p =  30*(j+1)
        circle.color('#F01F41')
        circle.goto(-p,-q+280)
        circle.stamp()
        circle.goto(p,-q+280)
        circle.stamp()        
        r += 2
    if i % 4 == 3:
        p =  30*(j+1)
        circle.color('#FBFA59')
        circle.goto(-p,-q+280)
        circle.stamp()
        circle.goto(p,-q+280)
        circle.stamp() 
square.color('#9C661F')
for i in range(17,20):
    q = 30*i
    for j in range(3):    
        p = 30*j
        square.goto(p,-q+280)
        square.stamp()
        square.goto(-p,-q+280)
        square.stamp()        
        
turtle.exitonclick()
