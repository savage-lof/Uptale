import pygame
import time
import os
import sys


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


def main():
    pygame.init()
    size = width, height = 800, 800
    screen = pygame.display.set_mode(size)
    image = load_image("first.jpg")
    image1 = pygame.transform.scale(image, (800, 800))
    screen.blit(image1, (0, 0))
    pygame.display.flip()
    time.sleep(2)
    image = load_image("menu.jpg")
    screen.blit(image, (0, 0))
    pygame.display.flip()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if pygame.mouse.get_pos()[0] >= 80 and pygame.mouse.get_pos()[1] >= 285:
                if pygame.mouse.get_pos()[0] <= 515 and pygame.mouse.get_pos()[1] <= 370:
                    pass
                    # new game
            if pygame.mouse.get_pos()[0] >= 80 and pygame.mouse.get_pos()[1] >= 441:
                if pygame.mouse.get_pos()[0] <= 565 and pygame.mouse.get_pos()[1] <= 515:
                    pass
                    # prodolgit game
            if pygame.mouse.get_pos()[0] >= 80 and pygame.mouse.get_pos()[1] >= 614:
                if pygame.mouse.get_pos()[0] <= 330 and pygame.mouse.get_pos()[1] <= 685:
                    pass
                    # exit
        pygame.display.flip()
    pygame.quit()


if __name__ == "__main__":
    main()
