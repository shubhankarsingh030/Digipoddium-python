from turtle import *
speed ("fastest")

i = 1
while True:
    fd(10+ i)
    left(360/4)
    i += 5
    write(i)
    if i > 500:
        break
mainloop()