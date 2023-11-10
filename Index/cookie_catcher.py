import pgzrun
import random

WIDTH = 1200
HEIGHT = 500

p = Actor('ironman',(50,50))
p.speed = 10

rx = random.randint(50, WIDTH-50)
ry = random.randint(50, HEIGHT-50)
c = Actor('cookie_img',(rx,ry))

score = 0

def draw():
    if score <= 10:
        screen.clear()
        p.draw()
        c.draw()
        screen.draw.text(f'Score : {score}', (WIDTH-120,10), fontsize=30)
        screen.draw.text('WASD to move',(10,10),fontsize=30)
    else:
        screen.fill('blue')
        screen.draw.text('yohooo!!!! YOU WIN',(WIDTH/2-100,HEIGHT/2-50), fontsize=50)

def player_control():
    if keyboard.W:
        p.y -= p.speed
    elif keyboard.S:
        p.y += p.speed
    elif keyboard.A:
        p.x -= p.speed
        p.angle = +90
    elif keyboard.D:
        p.x += p.speed
        p.angle = -90
    else:
        p.angle = 0

    #boundar line
    if p.x < 0:
        p.x = WIDTH
    if p.x > WIDTH:
        p.x = 0
    if p.y < 0:
        p.y = HEIGHT
    if p.y > HEIGHT:
        p.y = 0
    
def handle_score():
    global score
    if p.colliderect(c):
        rx = random.randint(50, WIDTH-50)
        ry = random.randint(50, HEIGHT-50)
        c.pos = (rx,ry)
        score += 1

def update():
    player_control()
    handle_score()

pgzrun.go()
