import pygame
from TestGamePlay import gg_sprite, gg_left, gg_right, all_sprites, camera, width, height, walls, screen, gg_stop_l, \
    gg_stop_r

fps = 144
clock = pygame.time.Clock()
s = 2
move_right = False
move_left = False
move_up = False
move_down = False
move = False
direction = 2
running = True
while running:
    gg_stop_l.rect = gg_sprite.rect
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            move_left = True
            move = True
            direction = 1
            gg_sprite.frames = gg_left.frames
        if event.type == pygame.KEYUP and event.key == pygame.K_LEFT:
            move_left = False
            move = False

        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            move_right = True
            move = True
            direction = 2
            gg_sprite.frames = gg_right.frames
        if event.type == pygame.KEYUP and event.key == pygame.K_RIGHT:
            move_right = False
            move = False

        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            move_up = True
            move = True
            if direction == 1:
                gg_sprite.frames = gg_left.frames
            elif direction == 2:
                gg_sprite.frames = gg_right.frames
        if event.type == pygame.KEYUP and event.key == pygame.K_UP:
            move_up = False

        if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            move_down = True
            if direction == 1:
                gg_sprite.frames = gg_left.frames
            elif direction == 2:
                gg_sprite.frames = gg_right.frames
        if event.type == pygame.KEYUP and event.key == pygame.K_DOWN:
            move_down = False
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
    screen.fill(pygame.Color("black"))
    all_sprites.draw(screen)
    all_sprites.update()
    clock.tick(150)
    pygame.display.flip()

pygame.quit()
