#green plants drawing


import turtle as t
t.speed(0)
t.color("#4d1919")
t.width(5)


def go_to_Pos(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
    
def Cute_leaves(x):
    t.width(1)
    t.fd(20)
    t.right(60)
    t.begin_fill()
    t.fillcolor("Green")
    t.circle(x/2,90)
    t.fd(x/2)
    t.lt(127)
    t.fd(x/2)
    t.circle(x/2,90)
    t.end_fill()
    
    t.left(115)
    t.width(0.1)
    t.fd(x)
    t.color("#bfff00")
    
    for i in range(4):
        t.backward(x/4)
        t.width(2/(4-i))
        t.left(30)
        t.fd(x/(7-i))
        t.backward(x/(7-i))
        t.right(60)
        t.fd(x/(7-i))
        t.backward(x/(7-i))
        t.left(30)
    t.width(5)
    t.color("#4d1919")
    t.backward(20)
    
def branches():  
    for b in range(3):
        t.seth(30*(b+1))
        go_to_Pos(0,-250)
        n = 12
        
        for i in range(n):
            angle = 45 if i %2 else -45
            t.circle(500,4)
            t.right(angle)
            Cute_leaves(80+((n-i)*2))
            t.left(angle)
            
        Cute_leaves(80)
        

def Pot():
    go_to_Pos(2,-250)
    t.seth(-90)
    t.width(10)
    t.begin_fill()
    t.fd(30)
    t.seth(0)
    t.fd(30)
    t.seth(-100)
    t.fd(40)
    t.seth(180)
    t.fd(50)
    t.seth(100)
    t.fd(40)
    t.seth(0)
    t.fd(30)
    t.end_fill()
    
    
branches()
Pot()
t.done()
