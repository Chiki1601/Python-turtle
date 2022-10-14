#print your name wallpaper
from turtle import*
bgcolor("black")

colors= ["red","yellow","orange","green","blue","pink","purple"]
name = textinput("Enter your name","Enter your name")
s = int(numinput("Enter no. of sides","How many sides you want"))
for i in range(100):
    pencolor(colors[i%s%7])
    pu()
    fd(i*5)
    pd()
    write(name,font = {"",int((i*2+4)/4),"bold"})
    lt(360/s+4)
ht()
done()
