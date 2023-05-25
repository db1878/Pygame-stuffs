#Import Libraries
import pygame
from pygame.locals import*

#Initialise pygame
pygame.init()

#declare screen size
screen_width = 1024
screen_height = 736

#Window
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Camera')

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



    pygame.display.update()

pygame.quit()
