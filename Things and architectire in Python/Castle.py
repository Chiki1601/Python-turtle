Program:
# Castle drawing using turtle

import turtle

def polygon(a_turtle, num_side, side_length):
    '''
    The function draws a regular ploygon with the given number of sides, each
    side of the given length.
    a_turtle (turtle) - The turtle that is drawing.
    num_side (int) - Number of sides of the polygon.
    side_lenth (int) - Length of each side of the the polygon.
    '''
    
    for i in range(num_side):
        a_turtle.forward(side_length)
        a_turtle.left(360/num_side)

def house(a_turtle, size):
    '''
    Draw a simple house of the given size.
    
    a_turtle (turtle) - The turtle that is drawing.
    size (int) - Length of each side of the the polygon.
    '''
    polygon(a_turtle, 4, size)
    a_turtle.left(90)
    a_turtle.forward(size)
    a_turtle.right(90)
    polygon(a_turtle, 3,size)
    a_turtle.left(90)
    a_turtle.backward(size)
    a_turtle.right(90)
    return None

def castle(a_turtle, size):
    '''
    Draw a simple castle of the given size.
    a_turtle (turtle) - The turtle that is drawing.
    size (int) - Length of each side of the the polygon.
    '''
    polygon(a_turtle, 4, size)
    a_turtle.penup()
    a_turtle.backward(size * 0.25)
    a_turtle.left(90)
    a_turtle.forward(size)
    a_turtle.right(90)
    a_turtle.pendown()
    house(a_turtle, size * 0.5)
    a_turtle.forward(size * 0.5)
    house(a_turtle, size * 0.5)
    a_turtle.forward(size * 0.5)
    house(a_turtle, size * 0.5)
    a_turtle.penup()
    a_turtle.backward(size * 0.75)
    a_turtle.left(90)
    a_turtle.backward(size)
    a_turtle.right(90)
    a_turtle.pendown()
    return None

#==============================================
def main():
    '''Draw a castle.'''
    yertle = turtle.Turtle()
    yertle.speed(0)
    yertle.penup()
    yertle.backward(100)
    yertle.pendown()
    yertle.pencolor('dark slate grey')
    yertle.pensize(5)

    for i in range(4):
       castle(yertle, 100)
       yertle.forward(100)


    yertle.left(180)
    for i in range(4):
        castle(yertle, 100)
        yertle.forward(100)



    # A test to create a castle manually  

    '''
    for i in range(9):
        polygon(yertle, 3, 20)
        yertle.penup()
        yertle.backward(20)
        yertle.pendown()
    yertle.penup()
    yertle.forward(20)
    yertle.right(90)
    yertle.forward(20)
    yertle.left(90)
    yertle.pendown()
    for i in range(9):
        polygon(yertle, 4, 20)
        yertle.forward(20)
    yertle.backward(10)
    yertle.left(180)
    for i in range(4):
        polygon(yertle, 4, 40)
        yertle.forward(40)    
    
    yertle.left(90)
    yertle.forward(80)
    yertle.left(90)
    for i in range(4):
        polygon(yertle, 4, 40)
        yertle.forward(40)
    yertle.penup()
    yertle.backward(10)
    yertle.right(90)
    yertle.forward(20)
    yertle.left(90)
    yertle.pendown()
    for i in range(9):
        polygon(yertle, 4, 20)
        yertle.penup()
        yertle.backward(20)
        yertle.pendown()
    yertle.penup()
    yertle.forward(20)
    yertle.pendown()
     
    for i in range(9):
        yertle.right(60)
        polygon(yertle, 3, 20)
        yertle.left(60)
        yertle.forward(20)
    '''

    input('Enter to end')

if __name__ == '__main__':
    main()
