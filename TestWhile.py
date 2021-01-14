import pygame
import time
from TestLoadGame import load_image
from TestGame import game, main
from screen import screen
import sqlite3

pygame.init()
con = sqlite3.connect("uptale.db")
cur = con.cursor()
result = cur.execute("""SELECT * FROM save ORDER BY ID DESC LIMIT 1""").fetchone()
rect = (result[1], result[2])
file = result[3]


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
                        main()
                if pygame.mouse.get_pos()[0] >= 80 and pygame.mouse.get_pos()[1] >= 441:
                    if pygame.mouse.get_pos()[0] <= 565 and pygame.mouse.get_pos()[1] <= 515:
                        print(result)
                        main(file, rect)
                if pygame.mouse.get_pos()[0] >= 80 and pygame.mouse.get_pos()[1] >= 614:
                    if pygame.mouse.get_pos()[0] <= 330 and pygame.mouse.get_pos()[1] <= 685:
                        running = False
    pygame.quit()


if __name__ == '__main__':
    start()
