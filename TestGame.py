import pygame
from TestLvl import gg_sprite, gg_left, gg_right, all_sprites, walls, gg_stop_l, \
    gg_stop_r, npc, chest
from TestClassCamera import Camera
from TestScroll import Scroll
from TestStartScreen import screen_start
from screen import screen, width, height

pygame.font.init()
fps = 144
clock = pygame.time.Clock()
s = 2
f2 = pygame.font.Font(None, 48)
f3 = pygame.font.Font(None, 48)
text2 = f2.render("Press N", False, pygame.Color("white"))
text3 = f3.render("Press F", False, pygame.Color("white"))
sprites_note = pygame.sprite.Group()
camera = Camera()


def game():
    move_right = False
    move_left = False
    move_up = False
    move_down = False
    move = False
    direction = 2
    text1 = False
    f_press = False
    n_press = False
    running = True
    scrolling = False
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

            if event.type == pygame.KEYUP and event.key == pygame.K_n:
                if n_press:
                    screen_start()

            if event.type == pygame.KEYUP and event.key == pygame.K_f:
                if f_press:
                    scroll = Scroll(sprites_note, ['Во время игры вам будут попадаться записки',
                                                   'В них будут вложены подказки по игре и',
                                                   'сюжету.'])
                    sprites_note.add(scroll)
                    screen.blit(scroll.image, scroll.rect)
                    scroll.read()
                    scrolling = True

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
        if text1:
            sprites_note.draw(screen)
            scroll.read()
        if pygame.sprite.collide_rect(gg_stop_l, npc):
            screen.blit(text2, (350, 600))
            n_press = True
        if pygame.sprite.collide_rect(gg_stop_l, chest):
            screen.blit(text3, (350, 600))
            f_press = True
        pygame.display.update()
        pygame.display.flip()

    pygame.quit()
