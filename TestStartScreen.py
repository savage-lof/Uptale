import pygame
import sys
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
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pos()[0] in range(125, 690) and pygame.mouse.get_pos()[1] in range(360, 425):
                        f = open('save.txt', 'w')
                        a = 'adaasdafqwf'
                        f.write(a)
                        f.close()
                if pygame.mouse.get_pos()[0] in range(95, 706) and pygame.mouse.get_pos()[1] in range(507, 568):
                    running = False
                if pygame.mouse.get_pos()[0] in range(255, 550) and pygame.mouse.get_pos()[1] in range(642, 693):
                    pygame.quit()
                    sys.exit()

        all_sprites.draw(screen)
        vehicle.update(fps)
        clock.tick(fps)
        pygame.display.flip()
