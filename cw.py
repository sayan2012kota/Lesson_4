import pgzrun
from random import randint

TITLE = "Alien Game"
WIDTH = 500
HEIGHT = 500

#variable to store message
message = ""

#actor is a built in object in pgzero
#similar to sprites in scratch

alien = Actor('alien_img')
#alien.pos = 50,50

def draw():
    screen.clear()
    screen.fill(color = (128,0,0))

    alien.draw()

    #Write text on the screen for message
    screen.draw.text(message , center = (400,10) ,  fontsize = 30 )

def place_alien():
    alien.x = randint(50 , WIDTH - 50)
    alien.y = randint ( 50 , HEIGHT - 50 )

def on_mouse_down(pos):
    global message
    if alien.collidepoint(pos):
        message = "Good shot"
        place_alien()
    else :
        message = "You missed"

place_alien()


pgzrun.go()