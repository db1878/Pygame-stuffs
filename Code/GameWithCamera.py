#Import Libraries
import pygame
from pygame.locals import*
from setting import *
from level import Level

#Initialise pygame
pygame.init()





#Window
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Camera')

level = Level(level_map, screen)

#set fps
fps = 60
clock = pygame.time.Clock()

#game loop
run = True
while run:

    #set fps p.2
    clock.tick(fps)

    # event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    level.run()



    pygame.display.update()

pygame.quit()
