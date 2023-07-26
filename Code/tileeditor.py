import pygame

pygame.init()


#game window

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 640
LOWER_MARGIN = 100
SIDE_MARGIN = 300

screen = pygame.display.set_mode((SCREEN_WIDTH + SIDE_MARGIN, SCREEN_HEIGHT + LOWER_MARGIN))
pygame.display.set_caption('level editor')

#load images




run = True
while run:
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()