from cgitb import grey
from turtle import * 

speed ('fastest')
side = 10
for i in range(side):
    pencolor('purple')
    pensize(2)
    fd(100)
    lt(360/side)
    dot(side*5)
    pensize (10)
    pencolor('pink')
    circle(side*10)

mainloop()