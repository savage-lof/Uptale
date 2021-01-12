import pygame

from TestAnimation import AnimatedSprite
from TestClassCamera import Camera
from TestClassTile import Tile
from TestLoadGame import load_image, all_sprites
from TestScroll import Scroll, Diolog
from TestStartScreen import screen_start
from screen import screen, width, height

pygame.font.init()
sprites_note = pygame.sprite.Group()
sprites = pygame.sprite.Group()
fps = 144
clock = pygame.time.Clock()
s = 2
f2 = pygame.font.Font(None, 48)
f3 = pygame.font.Font(None, 48)
text2 = f2.render("Press N", False, pygame.Color("white"))
text3 = f3.render("Press F", False, pygame.Color("white"))
camera = Camera()
scroll = Scroll(sprites_note, ['Во время игры вам будут попадаться записки',
                               'В них будут вложены подказки по игре и',
                               'сюжету.'])

scroll_npc = Diolog(sprites_note, ['Дарова странник!',
                                   'Я призвал тебя!',
                                   'Ты должен стать героем, а для этого',
                                   ' иди вперёд и убей короля',
                                   ' демооооонов'])
sprites_note.remove(scroll, scroll_npc)


def lvl1(rect):
    walls = list()
    walls.append(Tile('up_wall_new.png', (850, 450 - 378), 'wall'))
    walls.append(Tile('dawn_wall.png', (850, 450 + 310), 'wall'))
    walls.append(Tile('side_wall.png', (850 - 240, 450 - 68), 'wall'))
    walls.append(Tile('side_wall.png', (850 + 240, 450 - 68), 'wall'))
    floor = Tile('floor.png', (850, 450), 'floor')
    floor = Tile('floor_new.png', (850, 450), 'floor')
    npc = AnimatedSprite(load_image("npc_mir.png"), 3, 1, 735, 105, all_sprites, 35)
    walls.append(npc)
    gerl = AnimatedSprite(load_image("gerl.png"), 1, 7, 600, 50, all_sprites, 15)
    walls.append(AnimatedSprite(load_image('el.png'), 9, 1, 850 - 51, 20, all_sprites, 35))
    chest = Tile('chest.png', (1000, 150), 'floor')
    gg_right = AnimatedSprite(load_image("right_player.png"), 8, 1, rect[0], rect[1], sprites, 15)
    gg_left = AnimatedSprite(load_image("left_player.png"), 8, 1, rect[0], rect[1], sprites, 15)
    gg_sprite = AnimatedSprite(load_image("right_player_stop.png"), 1, 1, rect[0], rect[1], all_sprites, 15)
    gg_stop_r = AnimatedSprite(load_image("right_player_stop.png"), 1, 1, rect[0], rect[1], sprites, 15)
    gg_stop_l = AnimatedSprite(load_image("left_player_stop.png"), 1, 1, rect[0], rect[1], sprites, 15)
    words = ['Во время игры вам будут попадаться записки',
             'В них будут вложены подказки по игре и',
             'сюжету. После прочтения записок вы попадете',
             'на следующий уровень']
    game(walls, floor, chest, gg_right, gg_left, gg_sprite, gg_stop_r, gg_stop_l,
         npc, words, gg_rect=gg_sprite.rect, lvl='txt1.txt')

def lvl2(rect):
    walls = list()
    walls.append(Tile('up_wall_lvl2.png', (850, 450 - 226), 'wall'))
    walls.append(Tile('dawn_wall_lvl2.png', (850, 450 + 160), 'wall'))
    walls.append(Tile('side_wall_Lvl2.png', (850 - 695, 450 - 66), 'wall'))
    walls.append(Tile('side_wall_Lvl2.png', (850 + 695, 450 - 66), 'wall'))
    floor = Tile('floorLvl2.png', (850, 450), 'floor')
    npc = AnimatedSprite(load_image("npc_mir.png"), 3, 1, 750, 500, all_sprites, 30)
    walls.append(npc)
    chest = Tile('chest.png', (350, 325), 'wall')
    gg_right = AnimatedSprite(load_image("right_player.png"), 8, 1, rect[0], rect[1], sprites, 15)
    gg_left = AnimatedSprite(load_image("left_player.png"), 8, 1, rect[0], rect[1], sprites, 15)
    gg_sprite = AnimatedSprite(load_image("right_player_stop.png"), 1, 1, rect[0], rect[1], all_sprites, 15)
    gg_stop_r = AnimatedSprite(load_image("right_player_stop.png"), 1, 1, rect[0], rect[1], sprites, 15)
    gg_stop_l = AnimatedSprite(load_image("left_player_stop.png"), 1, 1, rect[0], rect[1], sprites, 15)
    words = ['Будте готовы встретить ']
    game(walls, floor, chest, gg_right, gg_left, gg_sprite, gg_stop_r, gg_stop_l,
         npc, words, gg_rect=gg_sprite.rect, lvl='txt2.txt')


def lvl3(rect):
    walls = list()
    walls.append(Tile('up_wall_lvl1.png', (850, 450 - 378), 'wall'))
    walls.append(Tile('dawn_wall_lvl1.png', (850, 450 + 310), 'wall'))
    walls.append(Tile('side_wall.png', (850 - 468, 450 - 68), 'wall'))
    walls.append(Tile('side_wall.png', (850 + 468, 450 - 68), 'wall'))
    floor = Tile('floorLvl1.png', (850, 450), 'floor')
    npc = AnimatedSprite(load_image("npc.png"), 11, 1, 750, 100, all_sprites, 25)
    walls.append(npc)
    chest = Tile('chest.png', (350, 325), 'wall')
    gg_right = AnimatedSprite(load_image("right_player.png"), 8, 1, 850, 450, sprites, 15)
    gg_left = AnimatedSprite(load_image("left_player.png"), 8, 1, 850, 450, sprites, 15)
    gg_sprite = AnimatedSprite(load_image("right_player_stop.png"), 1, 1, 850, 450, all_sprites, 15)
    gg_stop_r = AnimatedSprite(load_image("right_player_stop.png"), 1, 1, 850, 450, sprites, 15)
    gg_stop_l = AnimatedSprite(load_image("left_player_stop.png"), 1, 1, 850, 450, sprites, 15)
    game(walls, floor, chest, gg_right, gg_left, gg_sprite, gg_stop_r, gg_stop_l,
         npc, words, gg_rect=gg_sprite.rect, lvl='txt2.txt')

def game(walls, floor, chest, gg_right, gg_left, gg_sprite, gg_stop_r, gg_stop_l,
         npc, gg_rect=None, lvl=None):
    move_right = False
    move_left = False
    move_up = False
    move_down = False
    text1 = False
    text4 = False
    direction = 2
    f_press = False
    n_press = False
    running = True
    while running:
        screen.fill(pygame.Color("black"))
        gg_stop_l.rect = gg_sprite.rect
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and (event.key == pygame.K_LEFT or event.key == pygame.K_a):
                move_left = True
                direction = 1
                gg_sprite.frames = gg_left.frames
            if event.type == pygame.KEYUP and (event.key == pygame.K_LEFT or event.key == pygame.K_a):
                move_left = False

            if event.type == pygame.KEYDOWN and (event.key == pygame.K_RIGHT or event.key == pygame.K_d):
                move_right = True
                direction = 2
                gg_sprite.frames = gg_right.frames
            if event.type == pygame.KEYUP and (event.key == pygame.K_RIGHT or event.key == pygame.K_d):
                move_right = False

            if event.type == pygame.KEYDOWN and (event.key == pygame.K_UP or event.key == pygame.K_w):
                move_up = True
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
                    if not text4:
                        sprites_note.add(scroll_npc)
                        text4 = True
                    else:
                        sprites_note.remove(scroll_npc)
                        text4 = False

            if event.type == pygame.KEYUP and event.key == pygame.K_f:
                if f_press:
                    if not text1:
                        sprites_note.add(scroll)
                        text1 = True
                    else:
                        sprites_note.remove(scroll)
                        text1 = False
                        return

        camera.update(gg_sprite, width, height)
        for sprite in all_sprites:
            camera.apply(sprite)
        if not text1:
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
            screen.blit(text2, (350, 600))
            n_press = True
        if pygame.sprite.collide_rect(gg_stop_l, chest):
            screen.blit(text3, (350, 600))
            f_press = True
        if text1:
            sprites_note.draw(screen)
            scroll.read()
        if text4:
            sprites_note.draw(screen)
            scroll_npc.read()
        pygame.display.update()
        pygame.display.flip()

    pygame.quit()


def main(file='lvl3.txt', rect=None):
    if file == 'lvl1.txt':
        lvl1(rect=(850, 450))
        file = 'lvl2.txt'
        clean()
    if file == 'lvl2.txt':
        lvl2(rect=(350, 450))
        file = 'lvl3.txt'
        clean()
    if file == 'lvl3.txt':
        lvl3(rect)


def clean():
    all_sprites.empty()
    sprites.empty()
    sprites_note.empty()

