#awesome Design 38

import turtle as t 


t.bgcolor("black")
t.pensize(3)
t.speed(6)
t.pu()
t.goto(-110,0)
t.pd()

for i in range(21):
    t.pencolor("red")
    t.lt(9)
    t.fd(150)
    t.lt(90)
    t.pencolor("#8A52FB")
    t.fd(80)
    t.pencolor("#11EE05")
    t.circle(-70,90)
    t.circle(-70,90)
    t.pencolor("#8A52FB")
    t.backward(80)
    t.rt(45)
    t.pencolor("red")
    t.fd(100)
    
t.ht()
t.done()
