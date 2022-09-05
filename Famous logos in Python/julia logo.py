#julia logo in Python

import turtle as t
r = 50
t.color("green")
t.begin_fill()
t.circle(r)
t.end_fill()

t.pu()
t.goto(-70,-90)
t.color("maroon")
t.begin_fill()
t.circle(r)
t.end_fill()
t.pd()

t.pu()
t.goto(50,-100)
t.color("#C45AEC")
t.begin_fill()
t.circle(r)
t.end_fill()
t.pd()

t.done()
