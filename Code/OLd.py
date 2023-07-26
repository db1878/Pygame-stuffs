# import libraries
import Map
import pygame
from pytmx.util_pygame import load_pygame

# initialise pygame
pygame.init()

#

# create a class
class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, surf, groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_rect(topleft=pos)


# createsprite
sprite_group = pygame.sprite.Group()

# game window
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 608

# create game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("DeepDivin")


#spritesheet
sprite_sheet_image = pygame.image.load('C:/Users/decla/OneDrive/PythonGameProject/Map/Characters/Octo_Walk.png').convert_alpha()


# rectangles x=200 y=100 width = 150 height=100
rect1 = pygame.Rect(200, 100, 150, 100)


# fps
clock = pygame.time.Clock()

# tmx file
tmx_data = load_pygame('../Map/Graphics/Deep.tmx')

# cycle through all layers
for layer in tmx_data.visible_layers:
    if hasattr(layer, 'data'):
        for x, y, surf in layer.tiles():
            pos = (x * 16, y * 16)
            Tile(pos=pos, surf=surf, groups=sprite_group)
# get all layers
print(tmx_data.layers)

# get tiles
layer = tmx_data.get_layer_by_name('Background')
# for x, y, surf in layer.tiles():
# print(x)
# print(y)
# print(surf)

# game loop
run = True
while run:

    # fps
    clock.tick(60)


    #draw
    sprite_group.draw(screen)

    #draw sprite#
    screen.blit(sprite_sheet_image, (0,0))

    # event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    sprite_group.draw(screen)

    pygame.display.update()

pygame.quit()