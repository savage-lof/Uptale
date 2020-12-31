import pygame
from TestClassTile import Tile, Tile_player
from TestClassCamera import Camera
from TestLoadGame import all_sprites
from TestAnimation import AnimatedSprite
from TestLoadGame import load_image

pygame.font.init()
sprites = pygame.sprite.Group()

size = width, height = 800, 800
screen = pygame.display.set_mode(size)
walls = list()

walls.append(Tile('up_wall.png', (850, 450 - 378), 'wall'))
walls.append(Tile('dawn_wall.png', (850, 450 + 310), 'wall'))
walls.append(Tile('side_wall.png', (850 - 240, 450 - 68), 'wall'))
walls.append(Tile('side_wall.png', (850 + 240, 450 - 68), 'wall'))
floor = Tile('floor.png', (850, 450), 'floor')

dragon = AnimatedSprite(load_image("pygame-8-1 (1).png"), 8, 2, 608, 120, all_sprites)
mask_dragon = pygame.mask.from_surface(dragon.image)
walls.append(dragon)
sprite_press_dragon = pygame.sprite.Sprite()
sprite_press_dragon.image = dragon.frames[0]
sprite_press_dragon.rect = dragon.rect

gg_right = AnimatedSprite(load_image("right_player.png"), 8, 1, 850, 450, sprites)
gg_left = AnimatedSprite(load_image("left_player.png"), 8, 1, 850, 450, sprites)
gg_sprite = AnimatedSprite(load_image("right_player_stop.png"), 1, 1, 850, 450, all_sprites)
gg_stop_r = AnimatedSprite(load_image("right_player_stop.png"), 1, 1, 850, 450, sprites)
gg_stop_l = AnimatedSprite(load_image("left_player_stop.png"), 1, 1, 850, 450, sprites)

f2 = pygame.font.Font(None, 48)
text2 = f2.render("Press F", False, pygame.Color("white"))

camera = Camera()
