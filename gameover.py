import os
import sys
import pygame

width, height = 1600, 900
screen = pygame.display.set_mode((width, height))


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)

    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()

    return image


class GameOver(pygame.sprite.Sprite):
    image = load_image("gameover.png")

    def __init__(self, *group):
        super().__init__(*group)
        self.image = GameOver.image
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


def over():
    all_sprites = pygame.sprite.Group()
    vehicle = GameOver(all_sprites)

    fps = 60
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(pygame.Color('blue'))
        all_sprites.draw(screen)
        vehicle.update(fps)
        clock.tick(fps)
        pygame.display.flip()
