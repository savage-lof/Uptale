import pygame
import time
from TestLoadGame import load_image
from TestGame import main
from screen import screen
from bd import result, first_result

pygame.init()


def start():
    image = load_image("first.jpg")
    image1 = pygame.transform.scale(image, (800, 800))
    screen.blit(image1, (0, 0))
    pygame.display.flip()
    time.sleep(1)
    image = load_image("menu.jpg")
    screen.blit(image, (0, 0))
    pygame.display.flip()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pos()[0] >= 80 and pygame.mouse.get_pos()[1] >= 285:
                    if pygame.mouse.get_pos()[0] <= 515 and pygame.mouse.get_pos()[1] <= 370:
                        main(first_result)
                if pygame.mouse.get_pos()[0] >= 80 and pygame.mouse.get_pos()[1] >= 441:
                    if pygame.mouse.get_pos()[0] <= 565 and pygame.mouse.get_pos()[1] <= 515:
                        main(result)
                if pygame.mouse.get_pos()[0] >= 80 and pygame.mouse.get_pos()[1] >= 614:
                    if pygame.mouse.get_pos()[0] <= 330 and pygame.mouse.get_pos()[1] <= 685:
                        running = False
    pygame.quit()


if __name__ == '__main__':
    start()
