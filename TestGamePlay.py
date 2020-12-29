import pygame
from TestClassTile import Tile, Tile_player
from TestClassCamera import Camera
from TestLoadGame import all_sprites
from TestAnimation import AnimatedSprite
from TestLoadGame import load_image

sprites = pygame.sprite.Group()

size = width, height = 800, 800
screen = pygame.display.set_mode(size)
walls = list()

walls.append(Tile('up_wall.png', (850, 450 - 378), 'wall'))
walls.append(Tile('dawn_wall.png', (850, 450 + 310), 'wall'))
walls.append(Tile('side_wall.png', (850 - 240, 450 - 68), 'wall'))
walls.append(Tile('side_wall.png', (850 + 240, 450 - 68), 'wall'))
floor = Tile('floor.png', (850, 450), 'floor')

gg_right = AnimatedSprite(load_image("right_player.png"), 8, 1, 850, 450, sprites)
gg_left = AnimatedSprite(load_image("left_player.png"), 8, 1, 850, 450, sprites)
gg_sprite = AnimatedSprite(load_image("right_player_stop.png"), 1, 1, 850, 450, all_sprites)
gg_stop_r = AnimatedSprite(load_image("right_player_stop.png"), 1, 1, 850, 450, sprites)
gg_stop_l = AnimatedSprite(load_image("left_player_stop.png"), 1, 1, 850, 450, sprites)

camera = Camera()
