import pygame
from TestLoadGame import load_image
width, height = 800, 800


class GameScreen(pygame.sprite.Sprite):
    image = load_image("newy.png")

    def __init__(self, *group):
        super().__init__(*group)
        self.image = GameScreen.image
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()
        self.x = -self.rect.width
        self.rect.x = -self.rect.width
        self.rect.y = 0
        self.speed = 600

    def update(self, fps):
        if self.x + self.rect.width >= width:
            return
        self.x += self.speed / fps
        self.x = min(self.x, 0)
        self.rect.x = self.x



