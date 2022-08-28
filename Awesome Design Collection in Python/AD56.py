#awesome design 56
import turtle as t 
import colorsys

t.bgcolor("black")
t.pensize(2)
t.speed(0)
n = 36

for i in range(60):
    c = colorsys.hsv_to_rgb(h,1,0.9)
    t.pencolor(c)
    h +=1/n
    t.fd(i*4)
    t.lt(100)
    t.fd(i*3.20)
    t.lt(200)
    
t.done()
