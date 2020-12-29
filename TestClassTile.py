import pygame
from TestLoadGame import load_image, all_sprites


class Tile(pygame.sprite.Sprite):

    def __init__(self, filename, center, type_is):
        image = load_image(filename, -1)
        super().__init__(all_sprites)
        self.image = image
        if type_is == 'wall':
            width, height = self.image.get_size()
            self.image = pygame.transform.scale(self.image, (width * 2, height * 2))
            self.rect = self.image.get_rect(
                center=center)
            self.mask = pygame.mask.from_surface(self.image)
        elif type_is == 'floor':
            width, height = self.image.get_size()
            self.image = pygame.transform.scale(self.image, (width * 2, height * 2))
            self.rect = self.image.get_rect(
                center=center)


class Tile_player(pygame.sprite.Sprite):
    def __init__(self, filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(
            filename).convert_alpha()
        self.mask = pygame.mask.from_surface(self.image)

        self.rect = self.image.get_rect(
            center=(850, 450))
