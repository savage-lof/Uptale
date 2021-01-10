import pygame
from TestClassTile import Tile, Tile_player
from TestLoadGame import all_sprites
from TestAnimation import AnimatedSprite
from TestLoadGame import load_image
from TestStartScreen import screen_start, screen, width, height

sprites = pygame.sprite.Group()
lvl = ['lvl1.txt']


for i in lvl:
    with open(f'{i}', mode="r", encoding="utf-8") as f:
        data = f.read().split('\n')
        for j in data:
            exec(j)
