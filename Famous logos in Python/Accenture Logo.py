#accenture logo in Python
from turtle import *


pu()
goto(-320,-100)
pd()
write("accenture",font=("Times Now",100,"normal"))

pu()
goto(10,70)
pd()
pencolor("#a35ecb")
fillcolor("#a35ecb")
begin_fill()

fd(1)
rt(90)
fd(50)
rt(-150)
fd(125)
rt(-30)
fd(50)
end_fill()
pu()
goto(71,178)
pd()
begin_fill()
fd(-50)
rt(150)
fd(-125)
rt(30)
fd(-50)

end_fill()

ht()
done()
