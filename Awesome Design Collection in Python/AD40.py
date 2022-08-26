#awesome design 40

import turtle as t

t.bgcolor("black")
cl = ['#9400d3','#4b0082',"#0000ff","#00ff00","#ffff00","#ff7f00","#ff0000"]

t.speed(11)
for i in range(10):
    t.pencolor(cl[i%7])
    t.rt(36*i)
    t.pu()
    t.fd(20)
    t.pd()
    for j in range(1,5):
        t.pu()
        t.fd(20)
        t.pd()
        t.fillcolor(cl[i%7])
        t.begin_fill()
        t.circle(j*2)
        t.end_fill()
    t.pu()
    t.fd(57)
    t.pd()
    
    for x in range(33):
        t.fillcolor(cl[i%7])
        t.begin_fill()
        t.circle(x*0.2)
        t.end_fill()
        t.rt(49)
        t.pu()
        t.fd(x+0.5)
        t.pd()
        
    t.pu()
    t.home()
    
t.ht()
t.done()
