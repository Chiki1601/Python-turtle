#method 1
from turtle import*
fd(100)  
rt(90)  
fd(100)  
rt(90)  
fd(100) 
rt(90)  
fd(100)  
hideturtle()
done()



#method 2
import turtle  
# Creating turtle  
t = turtle.Turtle()  
  
for i in range(4):  
    t.fd(100)  
    t.rt(90)  
  
  
turtle.mainloop()  
