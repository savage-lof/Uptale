import pygame
from TestStartSceenClass import GameScreen
from screen import screen


def screen_start():
    all_sprites = pygame.sprite.Group()
    vehicle = GameScreen(all_sprites)

    fps = 60
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        all_sprites.draw(screen)
        vehicle.update(fps)
        clock.tick(fps)
        pygame.display.flip()
