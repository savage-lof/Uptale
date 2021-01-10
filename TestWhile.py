import pygame
from TestLvl import gg_sprite, gg_left, gg_right, all_sprites, walls, gg_stop_l, \
    gg_stop_r, npc
from TestClassCamera import Camera
from TestStartScreen import screen_start, screen, width, height
import time
from TestLoadGame import load_image

pygame.font.init()
fps = 144
clock = pygame.time.Clock()
s = 2
f2 = pygame.font.Font(None, 48)
text2 = f2.render("Press F", False, pygame.Color("white"))
camera = Camera()


def start():
    pygame.init()
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
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pos()[0] >= 80 and pygame.mouse.get_pos()[1] >= 285:
                    if pygame.mouse.get_pos()[0] <= 515 and pygame.mouse.get_pos()[1] <= 370:
                        game()
                if pygame.mouse.get_pos()[0] >= 80 and pygame.mouse.get_pos()[1] >= 441:
                    if pygame.mouse.get_pos()[0] <= 565 and pygame.mouse.get_pos()[1] <= 515:
                        pass
                if pygame.mouse.get_pos()[0] >= 80 and pygame.mouse.get_pos()[1] >= 614:
                    if pygame.mouse.get_pos()[0] <= 330 and pygame.mouse.get_pos()[1] <= 685:
                        running = False
    pygame.quit()


def game():
    move_right = False
    move_left = False
    move_up = False
    move_down = False
    move = False
    direction = 2
    f_press = False
    running = True
    while running:
        screen.fill(pygame.Color("black"))
        gg_stop_l.rect = gg_sprite.rect
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and (event.key == pygame.K_LEFT or event.key == pygame.K_a):
                move_left = True
                move = True
                direction = 1
                gg_sprite.frames = gg_left.frames
            if event.type == pygame.KEYUP and (event.key == pygame.K_LEFT or event.key == pygame.K_a):
                move_left = False
                move = False

            if event.type == pygame.KEYDOWN and (event.key == pygame.K_RIGHT or event.key == pygame.K_d):
                move_right = True
                move = True
                direction = 2
                gg_sprite.frames = gg_right.frames
            if event.type == pygame.KEYUP and (event.key == pygame.K_RIGHT or event.key == pygame.K_d):
                move_right = False
                move = False

            if event.type == pygame.KEYDOWN and (event.key == pygame.K_UP or event.key == pygame.K_w):
                move_up = True
                move = True
                if direction == 1:
                    gg_sprite.frames = gg_left.frames
                elif direction == 2:
                    gg_sprite.frames = gg_right.frames
            if event.type == pygame.KEYUP and (event.key == pygame.K_UP or event.key == pygame.K_w):
                move_up = False

            if event.type == pygame.KEYDOWN and (event.key == pygame.K_DOWN or event.key == pygame.K_s):
                move_down = True
                if direction == 1:
                    gg_sprite.frames = gg_left.frames
                elif direction == 2:
                    gg_sprite.frames = gg_right.frames
            if event.type == pygame.KEYUP and (event.key == pygame.K_DOWN or event.key == pygame.K_s):
                move_down = False

            if event.type == pygame.KEYUP and event.key == pygame.K_f:
                if f_press:
                    screen_start()

        camera.update(gg_sprite, width, height)
        for sprite in all_sprites:
            camera.apply(sprite)

        if move_left:
            gg_sprite.rect.x -= s

        if move_right:
            gg_sprite.rect.x += s

        if move_down:
            gg_sprite.rect.y += s

        if move_up:
            gg_sprite.rect.y -= s

        if not move_right and not move_up and not move_left and not move_down:
            if direction == 1:
                gg_sprite.frames = gg_stop_l.frames
            elif direction == 2:
                gg_sprite.frames = gg_stop_r.frames

        for wall in walls:
            if pygame.sprite.collide_mask(gg_stop_l, wall):
                if move_up:
                    gg_sprite.rect.y += s
                if move_down:
                    gg_sprite.rect.y -= s
                if move_right:
                    gg_sprite.rect.x -= s
                if move_left:
                    gg_sprite.rect.x += s

        all_sprites.draw(screen)
        all_sprites.update()
        clock.tick(150)
        f_press = False
        if pygame.sprite.collide_rect(gg_stop_l, npc):
            screen.blit(text2, (350, 500))
            f_press = True
        pygame.display.update()
        pygame.display.flip()

    pygame.quit()


if __name__ == '__main__':
    start()
