import pygame

pygame.init()

#screen measurements
width = 800
height = int(width* 0.8)

screen = pygame.display.set_mode((width, height))

#title
pygame.display.set_caption('prototype 0.0.1')

#set fps
clock = pygame.time.Clock()
fps = 60


#define player action variables
moving_left = False
moving_right = False

#define colours
bg = (0, 191, 255)

def draw_bg():
    screen.fill(bg)

class Person(pygame.sprite.Sprite):
    def __init__(self,char_type, x, y, scale, speed):
        pygame.sprite.Sprite.__init__(self)
        self.char_type = char_type
        self.speed = speed
        self.direction = 1
        #1 = right -1 is left
        self.flip = False

        sprite_img = pygame.image.load(f'Map/Characters/Sprites/Hooded_idle_1.png')
        self.sprite_img = pygame.transform.scale(sprite_img, (int(sprite_img.get_width()* scale), int(sprite_img.get_height()* scale)))
        self.rect = self.sprite_img.get_rect()
        self.rect.center = (x, y)


    def move(self, moving_left, moving_right):
        #reset movement variables
        dx = 0
        dy = 0
        #change in y and x

        #assign movement variables if moving left or right
        if moving_left:
            dx = -self.speed
            self.flip = True
            self.direction = -1
        if moving_right:
            dx = self.speed
            self.flip = False
            self.direction = 1

        #update rect position
        self.rect.x += dx
        self.rect.y += dy


    

    def draw(self):
        screen.blit(pygame.transform.flip(self.sprite_img, self.flip, False), self.rect)


player = Person(200,200,3,5)
#200=x, 200=y 3=scale






run = True
while run:


    clock.tick(fps)

    draw_bg()

    #puts image onto rect
    player.draw()
    player.move(moving_left, moving_right)
    







    #event handler
    for event in pygame.event.get():
        #quit game
        if event.type == pygame.QUIT:
            run = False
        #keyboard presses
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                moving_left = True
            if event.key == pygame.K_d:
                moving_right = True
            if event.key == pygame.K_ESCAPE:
                run = False

        #keyboard button release
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                moving_left = False
            if event.key == pygame.K_d:
                moving_right = False
            


    pygame.display.update()

pygame.quit()