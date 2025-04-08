import pygame


display_width = 800
display_height = 600

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

pygame.init()
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('A Bit Racey')
clock = pygame.time.Clock()

minion_img_unscaled = pygame.image.load('minion2.png')
minion_img = pygame.transform.scale(minion_img_unscaled, (180,300))

minion_width = 175

def minion(x,y):
    gameDisplay.blit(minion_img, (x,y))

def game_loop():
    x = (display_width * 0.38)
    y = (display_height * 0.7)

    x_change = 0


    gameExit = False

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
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
        minion(x,y)

        if x > display_width - minion_width or x < 0:
            gameExit = True

        pygame.display.update()
        clock.tick(60)

game_loop()
pygame.quit()
quit()