import pygame
from TestLoadGame import load_image, all_sprites
from screen import screen, width, height


class Scroll(pygame.sprite.Sprite):
    image = load_image("scroll.png")

    def __init__(self, sprites, *words):
        super().__init__(sprites)
        self.image = Scroll.image
        self.rect = self.image.get_rect(center=(width // 2, height // 2))
        self.words = words

    def read(self):
        font = pygame.font.Font(None, 30)
        text_coord = 50
        for line in self.words:
            for words in line:
                string_rendered = font.render(words, 1, pygame.Color('black'))
                intro_rect = string_rendered.get_rect()
                text_coord += 10
                intro_rect.top = text_coord
                intro_rect.x = 10
                text_coord += intro_rect.height
                screen.blit(string_rendered, intro_rect)