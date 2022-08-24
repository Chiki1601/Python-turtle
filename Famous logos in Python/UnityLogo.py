#unity logo in Python

import turtle as t

t.left(90)


#inner triangle
t.begin_fill()
for i in range(3):
    t.forward(30)
    t.right(120)
t.end_fill()


def arrow():
    #left side of arrow
    t.begin_fill()
    t.forward(108)
    t.left(140)
    t.forward(103)
    t.right(140)
    t.forward(37.5)
    t.right(40)
    t.forward(127)
    t.right(100)
    
    
    #right side of arrow
    t.forward(127)
    t.right(40)
    t.forward(37.5)
    t.right(140)
    t.forward(103)
    t.left(139.5)
    t.forward(108)
    t.end_fill()
    
    
    t.right(29)
    t.forward(30)
    t.right(30)
    
t.left(90)    

for j in range(3):
    arrow()



t.done()
