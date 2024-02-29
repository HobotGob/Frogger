import pygame, sys
from settings import *
from player import Player
from Car import Car
from random import choice, randint


class AllSprites(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.offset = pygame.math.Vector2()
        self.bg = pygame.image.load('../Frogger/graphics/main/map_2.png').convert()
        self.fg = pygame.image.load('../Frogger/graphics/main/overlay_2.png').convert_alpha()

    def customize_draw(self):
        # change the offset vector
        self.offset.x = player.rect.centerx - WINDOW_WIDTH / 2
        self.offset.y = player.rect.centery - WINDOW_HEIGHT / 2

        # blit the bg
        display_surface.blit(self.bg, -self.offset)

        for sprite in sorted(self.sprites(), key=lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            display_surface.blit(sprite.image, offset_pos)

        display_surface.blit(self.fg, -self.offset)


# basic setup
pygame.init()
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Frogger')
clock = pygame.time.Clock()

# groups
all_sprites = AllSprites()
obstacle_sprites = pygame.sprite.Group()

# sprites
player = Player((950, 1600), all_sprites, obstacle_sprites)

# timer
car_timer = pygame.event.custom_type()
pygame.time.set_timer(car_timer, 50)
pos_list = []

# font
font = pygame.font.Font(None, 50)
text_surf = font.render('You Won!',True,'White')
text_rect = text_surf.get_rect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))

# music
music = pygame.mixer.Sound('../Frogger/audio/music.mp3')
music.play(loops = -1)

# game loop
while True:

    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == car_timer:
            random_pos = choice(CAR_START_POSITIONS)
            if random_pos not in pos_list:
                pos_list.append(random_pos)
                pos = (random_pos[0],random_pos[1] + randint(-8,8))
                Car(pos,[all_sprites, obstacle_sprites])
            if len(pos_list) > 5:
                del pos_list[0]




    # delta time
    dt = clock.tick() / 1000

    # draw a bg
    display_surface.fill('black')

    if player.pos.y >= 400:

        # update
        all_sprites.update(dt)

        # draw
        # all_sprites.draw
        all_sprites.customize_draw()
    else:
        display_surface.fill('teal')
        display_surface.blit(text_surf,text_rect)

    # update the display surface
    pygame.display.update()