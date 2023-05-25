import pygame

pygame.init()
pygame.display.set_caption("GAME")
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
#Height and width of the window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

player = pygame.Rect((300, 250, 50, 50))
#Assign a rectangle to the variable x=300 y=250 width = 50 height=50

import pygame
import random
pygame.init()
pygame.display.set_caption("GAME")
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
#Height and width of the window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

spaceship = pygame.image.load("spaceship_yellow.png").convert_alpha()

player = pygame.Rect((300, 250, 50, 50))
obstacle_rect = pygame.Rect(random.randint(0,500), random.randint(0, 300), 25, 25)

rect_1 = pygame.Rect(0,0, 150,100)
#rect_1.width = 400
#rect_1.height = 200
rect_2 = spaceship
rect_2 = spaceship.get_rect()
rect_2.topleft = (200,200)




#Assign a rectangle to the variable x=300 y=250 width = 50 height=50

clock = pygame.time.Clock()

run = True
while run:

    clock.tick(60)
    screen.fill((255, 255, 255))


    #draws the rectangle
    pygame.draw.rect(screen, (122,34,56),obstacle_rect)





    screen.blit(spaceship, rect_2)

    key = pygame.key.get_pressed()
    if key[pygame.K_a] == True:
        rect_2.x -=5
    elif key[pygame.K_d] == True:
        rect_2.x +=5
    elif key[pygame.K_s] == True:
        rect_2.y +=5
    elif key[pygame.K_w] == True:
        rect_2.y -=5


    #when a certain key is pressed the player moves


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False








    pygame.display.update()

pygame.quit()