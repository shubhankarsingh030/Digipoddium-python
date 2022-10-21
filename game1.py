import pgzrun
HEIGHT = 500
WIDTH = 800
def draw():
    #fill the screen colourwith blue
    screen.fill("blue")
    #display the image on the screen at (100,100) coordination
    screen.blit('ironman',(100,100))
pgzrun.go()