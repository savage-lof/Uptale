import pygame
from TestLoadGame import load_image, all_sprites
from screen import screen, width, height
pygame.font.init()


class Scroll(pygame.sprite.Sprite):
    image = load_image("scroll.png")

    def __init__(self, sprites, *words):
        super().__init__(sprites)
        self.image = Scroll.image
        self.rect = self.image.get_rect(center=(width // 2, height // 2))
        self.words = words

    def read(self):
        font = pygame.font.Font(None, 30)
        text_coord = 0
        for line in self.words:
            for word in line:
                string_rendered = font.render(word, False, pygame.Color('black'))
                intro_rect = string_rendered.get_rect()
                intro_rect.y = height // 2 + text_coord - 70
                intro_rect.x = width // 2 + text_coord - 225
                text_coord += 20
                screen.blit(string_rendered, intro_rect)