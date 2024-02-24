import pygame, sys
from settings import WINDOW_WIDTH, WINDOW_HEIGHT
from player import Player

# basic stuff
pygame.init()
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Frogger')
clock = pygame.time.Clock()

# groups
all_sprites = pygame.sprite.Group()

#sprites
player = Player((600, 400), all_sprites)

# game loop
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # delta time
    dt = clock.tick() / 1000

    # background
    display_surface.fill('black')

    # update
    all_sprites.update(dt)

    # draw
    all_sprites.draw(display_surface)

    # draw the frame
    pygame.display.update()