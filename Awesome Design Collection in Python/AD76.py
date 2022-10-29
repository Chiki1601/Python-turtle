#awesome design 76 
import turtle as t
import colorsys

t.bgcolor("black")
t.speed(0)
h = 0.0
for i in range(200):
     c = colorsys.hsv_to_rgb(h,1,1)
     t.pencolor(c)
     t.begin_fill()
     for j in range(6):
         t.lt(20)
         t.rt(50)
         t.lt(120)
         t.fd(i)
     t.rt(120)
     t.end_fill()
     h += 0.005
    
t.ht()
done()
