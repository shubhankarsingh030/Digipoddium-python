import pgzrun

HEIGHT = 500
WIDTH = 800

p = Actor('ironman',(100,100))
el = Actor ('cookie_img',(500,500))

def draw():
    screen.fill('purple')
    p.draw()
    el.draw()

def update():
    if keyboard.left:
        p.x -= 5
        p.angle = 10
    elif keyboard.right:
        p.x += 5
        p.angle = -10
    elif keyboard.up:
        p.y -= 5
    elif keyboard.down:
        p.y += 5
    elif keyboard.SPACE:
        p.angle = 180
    else:
        p.angle = 0
    #second actor control
    if p.x > el.x:
        el.x += 1
    if p.y > el.y:
        el.y += 1
    if p.x < el.x:
        el.x -= 1
    if p.y < el.y:
        el.y -= 1



pgzrun.go()