import pygame
import sys
from TestStartSceenClass import GameScreen, GameScreenWin
from screen import screen
from save import save


def screen_start(lvl, floor, wall_1, wall_2, wall_3, wall_4, chest, gg_left, gg_sprite, el, gerl, npc, npc_boss):
    all_sprites = pygame.sprite.Group()
    vehicle = GameScreen(all_sprites)

    fps = 60
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pos()[0] in range(125, 690) and pygame.mouse.get_pos()[1] in range(360, 425):
                    save(lvl, floor, wall_1, wall_2, wall_3, wall_4, chest, gg_left, gg_sprite, el, gerl, npc, npc_boss)
                if pygame.mouse.get_pos()[0] in range(95, 706) and pygame.mouse.get_pos()[1] in range(507, 568):
                    running = False
                if pygame.mouse.get_pos()[0] in range(255, 550) and pygame.mouse.get_pos()[1] in range(642, 693):
                    pygame.quit()
                    sys.exit()

        all_sprites.draw(screen)
        vehicle.update(fps)
        clock.tick(fps)
        pygame.display.flip()


def win():
    all_sprites = pygame.sprite.Group()
    vehicle = GameScreenWin(all_sprites)

    fps = 60
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.quit()
                sys.exit()

        all_sprites.draw(screen)
        vehicle.update(fps)
        clock.tick(fps)
        pygame.display.flip()
