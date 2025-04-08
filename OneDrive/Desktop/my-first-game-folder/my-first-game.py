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

def minion(x,y):
    gameDisplay.blit(minion_img, (x,y))

x = (display_width * 0.38)
y = (display_height * 0.7)


crashed = False

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

    
    gameDisplay.fill(white)
    minion(x,y)
    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()