import turtle
import math
import random

screen = turtle.Screen()
screen.setup(1000,1000)
screen.title("Random Cloud - PythonTurtle.Academy")

turtle.speed(0)
turtle.hideturtle()
turtle.up()
turtle.bgcolor('dodger blue')
turtle.pencolor('white')
turtle.pensize(2)

n = 500 # number of points on each ellipse
# X,Y is the center of ellipse, a is radius on x-axis, b is radius on y-axis
# ts is the starting angle of the ellipse, te is the ending angle of the ellipse
# P is the list of coordinates of the points on the ellipse
def ellipse(X,Y,a,b,ts,te,P):
    t = ts
    for i in range(n):
        x = a*math.cos(t)
        y = b*math.sin(t)
        P.append((x+X,y+Y))
        t += (te-ts)/(n-1)

# computes Euclidean distance between p1 and p2
def dist(p1,p2):
    return ((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)**0.5

# draws an arc from p1 to p2 with extent value ext
def draw_arc(p1,p2,ext):
    turtle.up()
    turtle.goto(p1)
    turtle.seth(turtle.towards(p2))
    a = turtle.heading() 
    b = 360-ext 
    c = (180-b)/2
    d = a-c
    e = d-90
    r = dist(p1,p2)/2/math.sin(math.radians(b/2)) # r is the radius of the arc
    turtle.seth(e) # e is initial heading of the circle
    turtle.down()
    turtle.circle(r,ext,100)
    return (turtle.xcor(),turtle.ycor()) # returns the landing position of the circle
                                         # this position should be extremely close to p2 but may not be exactly the same
                                         # return this for continuous drawing to the next point


def cloud(P):
    step = n//10 # draw about 10 arcs on top and bottom part of cloud
    a = 0 # a is index of first point
    b = a + random.randint(step//2,step*2) # b is index of second point
    p1 = P[a] # p1 is the position of the first point
    p2 = P[b] # p2 is the position of the second point
    turtle.fillcolor('white')
    turtle.begin_fill()
    p3 = draw_arc(p1,p2,random.uniform(70,180)) # draws the arc with random extention
    while b < len(P)-1:
        p1 = p3 # start from the end of the last arc 
        if b < len(P)/2: # first half is top, more ragged
            ext = random.uniform(70,180)
            b += random.randint(step//2,step*2)
        else: # second half is bottom, more smooth
            ext = random.uniform(30,70)
            b += random.randint(step,step*2)
        b = min(b,len(P)-1) # make sure to not skip past the last point
        p2 = P[b] # second point
        p3 = draw_arc(p1,p2,ext) # draws an arc and return the end position
    turtle.end_fill()

P = [] # starting from empty list
ellipse(0,0,300,200,0,math.pi,P) # taller top half
ellipse(0,0,300,50,math.pi,math.pi*2,P) # shorter bottom half
cloud(P)
