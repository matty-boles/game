import pygame
import time
import random

display_width = 800
display_height = 600

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

block_colour = (53, 155, 255)

pygame.init()
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('A Bit Racey')
clock = pygame.time.Clock()

minion_img_unscaled = pygame.image.load('minion3.xcf')
minion_img = pygame.transform.scale(minion_img_unscaled, (175,300))

minion_width = 160
minion_height = 300

def things_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Dodged: " + str(count), True, black)
    gameDisplay.blit(text,(0,0))


def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])

def minion(x,y):
    gameDisplay.blit(minion_img, (x,y))

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = (display_width*0.5, display_height*0.5)
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(2)

    game_loop()


def crash():
    message_display('You Crashed')


def game_loop():
    x = (display_width * 0.38)
    y = (display_height * 0.7)

    x_change = 0
    d = {}
    thing_count = 2

    for i in range(thing_count):
        d["thing_startx{0}".format(i)] = random.randrange(0,display_width)

    thing_starty = -600
    thing_speed = 4
    thing_width = 100
    thing_height = 100

    dodged = 0


    gameExit = False

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0


        x += x_change

        gameDisplay.fill(white)

        #things(thingx, thingy, thingw, thingh, color)
        for i in range(thing_count):
            things(d["thing_startx{0}".format(i)], thing_starty, thing_width, thing_height, block_colour)
            thing_starty += thing_speed

        minion(x,y)
        things_dodged(dodged)

        if x > display_width - minion_width or x < 0:
            crash()
        if thing_starty > display_height:   
            thing_starty = 0 - thing_height
            for i in range(thing_count):
                d["thing_startx{0}".format(i)] = random.randrange(0,display_width)
            dodged += 1
            thing_speed += 0.5
            #thing_width += (dodged*1.2)

        for i in range(thing_count):
            if x > d["thing_startx{0}".format(i)] - minion_width + 20 and x < d["thing_startx{0}".format(i)] + thing_width - 40:
                if y < thing_starty + thing_height - 40:
                    crash()
        pygame.display.update()
        clock.tick(60)

game_loop()
pygame.quit()
quit()