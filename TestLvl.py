import pygame
from TestClassTile import Tile, Tile_player
from TestLoadGame import all_sprites, load_image
from TestAnimation import AnimatedSprite
from screen import screen, size, width, height

sprites = pygame.sprite.Group()
lvl1 = 'lvl2.txt'
lvl2 = 'lvl1.txt'
with open(lvl1, mode="r", encoding="utf-8") as f:
    data = f.read().split('\n')
    for j in data:
        exec(j)




