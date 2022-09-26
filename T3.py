
from turtle import *

OUTSIDE = 6
INSIDE = 6

for i in range(OUTSIDE):
    fd (100)
    for j in range(INSIDE):
        fd (50)
        lt(360/INSIDE)
    lt(360/OUTSIDE)

mainloop()