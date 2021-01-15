import pygame

from TestStartScreen import screen_start, win
from TestAnimation import AnimatedSprite
from TestClassCamera import Camera
from TestClassTile import Tile
from TestLoadGame import load_image, all_sprites
from TestScroll import Scroll, Diolog
from screen import screen, width, height
from fighting import fighting
from save import save

pygame.font.init()
sprites_note = pygame.sprite.Group()
sprites = pygame.sprite.Group()
fps = 144
clock = pygame.time.Clock()
s = 2
f2 = pygame.font.Font(None, 48)
f3 = pygame.font.Font(None, 48)
f4 = pygame.font.Font(None, 48)
text2 = f2.render("Press N", False, pygame.Color("white"))
text3 = f3.render("Press F", False, pygame.Color("white"))
text5 = f4.render("Press E", False, pygame.Color("white"))
camera = Camera()
scroll = Scroll(sprites_note, ['Во время игры вам будут попадаться записки',
                               'В них будут вложены подказки по игре и',
                               'сюжету.'])
scroll2 = Scroll(sprites_note, ['Мало кому удавалось уйти отсюда живым'])
scroll3 = Scroll(sprites_note, ['Что ж удачи тебе'])

scroll_npc = Diolog(sprites_note, ['Дарова странник!',
                                   'Я призвал тебя!',
                                   'Ты должен стать героем, а для этого',
                                   ' иди вперёд и убей короля',
                                   ' демооооонов'])
scroll_npc2 = Diolog(sprites_note, ['Дарова ещё раз странник!',
                                    'Тебе прямо по коридору'])

sprites_note.remove(scroll, scroll2, scroll3, scroll_npc, scroll_npc2)


def lvl1(lvl='lvl1', wall_1_x=850, wall_1_y=72, wall_2_x=850, wall_2_y=760, wall_3_x=610,
         wall_3_y=382, wall_4_x=1090, wall_4_y=382, floor_x=850, floor_y=450, npc_x=735, npc_y=105,
         chest_x=735, chest_y=105, gg_left_x=850, gg_left_y=450, gg_sprite_x=850, gg_sprite_y=450,
         gerl_x=600, gerl_y=50, el_x=799, el_y=20, npc_boss_x=None, npc_boss_y=None):
    walls = list()
    wall_1 = Tile('up_wall_new.png', (wall_1_x, wall_1_y), 'wall')
    wall_2 = Tile('dawn_wall.png', (wall_2_x, wall_2_y), 'wall')
    wall_3 = Tile('side_wall.png', (wall_3_x, wall_3_y), 'wall')
    wall_4 = Tile('side_wall.png', (wall_4_x, wall_4_y), 'wall')
    walls.extend([wall_1, wall_2, wall_3, wall_4])
    floor = Tile('floor_new.png', (floor_x, floor_y), 'floor')
    npc = AnimatedSprite(load_image("npc_mir.png"), 3, 1, npc_x, npc_y, all_sprites, 35)
    walls.append(npc)
    gerl = AnimatedSprite(load_image("gerl.png"), 1, 7, gerl_x, gerl_y, all_sprites, 15)
    el = AnimatedSprite(load_image('el.png'), 9, 1, el_x, el_y, all_sprites, 35)
    walls.append(el)
    chest = Tile('chest.png', (chest_x, chest_y), 'floor')
    gg_right = AnimatedSprite(load_image("right_player.png"), 8, 1, gg_left_x, gg_left_y, sprites, 15)
    gg_left = AnimatedSprite(load_image("left_player.png"), 8, 1, gg_left_x, gg_left_y, sprites, 15)
    gg_sprite = AnimatedSprite(load_image("right_player_stop.png"), 1, 1, gg_sprite_x, gg_sprite_y, all_sprites, 15)
    gg_stop_r = AnimatedSprite(load_image("right_player_stop.png"), 1, 1, gg_left_x, gg_left_y, sprites, 15)
    gg_stop_l = AnimatedSprite(load_image("left_player_stop.png"), 1, 1, gg_sprite_x, gg_sprite_y, sprites, 15)
    game(walls, floor, wall_1, wall_2, wall_3, wall_4, chest, gg_right, gg_left, gg_sprite, gg_stop_r, gg_stop_l,
         'lvl1', el=el, gerl=gerl, npc=npc, npc_boss=None)


def lvl2(lvl='lvl2', wall_1_x=850, wall_1_y=224, wall_2_x=850, wall_2_y=610, wall_3_x=155,
         wall_3_y=384, wall_4_x=1545, wall_4_y=384, floor_x=850, floor_y=450, npc_x=750, npc_y=500,
         chest_x=350, chest_y=325, gg_left_x=350, gg_left_y=450, gg_sprite_x=350, gg_sprite_y=450,
         gerl_x=None, gerl_y=None, el_x=None, el_y=None, npc_boss_x=None, npc_boss_y=None):
    walls = list()
    wall_1 = Tile('up_wall_lvl2.png', (wall_1_x, wall_1_y), 'wall')
    wall_2 = Tile('dawn_wall_lvl2.png', (wall_2_x, wall_2_y), 'wall')
    wall_3 = Tile('side_wall_lvl2.png', (wall_3_x, wall_3_y), 'wall')
    wall_4 = Tile('side_wall_lvl2.png', (wall_4_x, wall_4_y), 'wall')
    walls.extend([wall_1, wall_2, wall_3, wall_4])
    floor = Tile('floorLvl2.png', (floor_x, floor_y), 'floor')
    npc = AnimatedSprite(load_image("npc_mir.png"), 3, 1, npc_x, npc_y, all_sprites, 30)
    walls.append(npc)
    chest = Tile('chest.png', (chest_x, chest_y), 'floor')
    gg_right = AnimatedSprite(load_image("right_player.png"), 8, 1, gg_left_x, gg_left_y, sprites, 15)
    gg_left = AnimatedSprite(load_image("left_player.png"), 8, 1, gg_left_x, gg_left_y, sprites, 15)
    gg_sprite = AnimatedSprite(load_image("right_player_stop.png"), 1, 1, gg_sprite_x, gg_sprite_y, all_sprites, 15)
    gg_stop_r = AnimatedSprite(load_image("right_player_stop.png"), 1, 1, gg_left_x, gg_left_y, sprites, 15)
    gg_stop_l = AnimatedSprite(load_image("left_player_stop.png"), 1, 1, gg_sprite_x, gg_sprite_y, sprites, 15)
    game(walls, floor, wall_1, wall_2, wall_3, wall_4, chest, gg_right, gg_left, gg_sprite, gg_stop_r, gg_stop_l,
         'lvl2', el=None, gerl=None, npc=npc, npc_boss=None)


def lvl3(lvl='lvl3', wall_1_x=850, wall_1_y=72, wall_2_x=850, wall_2_y=760, wall_3_x=382,
         wall_3_y=382, wall_4_x=1318, wall_4_y=382, floor_x=850, floor_y=450, npc_x=None, npc_y=None,
         chest_x=350, chest_y=350, gg_left_x=650, gg_left_y=450, gg_sprite_x=650, gg_sprite_y=450,
         gerl_x=None, gerl_y=None, el_x=None, el_y=None, npc_boss_x=750, npc_boss_y=100):
    walls = list()
    wall_1 = Tile('up_wall_lvl1.png', (wall_1_x, wall_1_y), 'wall')
    wall_2 = Tile('dawn_wall_lvl1.png', (wall_2_x, wall_2_y), 'wall')
    wall_3 = Tile('side_wall.png', (wall_3_x, wall_3_y), 'wall')
    wall_4 = Tile('side_wall.png', (wall_4_x, wall_4_y), 'wall')
    walls.extend([wall_1, wall_2, wall_3, wall_4])
    floor = Tile('floorLvl1.png', (floor_x, floor_y), 'floor')
    npc_boss = AnimatedSprite(load_image("npc.png"), 11, 1, npc_boss_x, npc_boss_y, all_sprites, 25)
    walls.append(npc_boss)
    chest = Tile('chest.png', (chest_x, chest_y), 'floor')
    gg_right = AnimatedSprite(load_image("right_player.png"), 8, 1, gg_left_x, gg_left_y, sprites, 15)
    gg_left = AnimatedSprite(load_image("left_player.png"), 8, 1, gg_left_x, gg_left_y, sprites, 15)
    gg_sprite = AnimatedSprite(load_image("right_player_stop.png"), 1, 1, gg_sprite_x, gg_sprite_y, all_sprites, 15)
    gg_stop_r = AnimatedSprite(load_image("right_player_stop.png"), 1, 1, gg_left_x, gg_left_y, sprites, 15)
    gg_stop_l = AnimatedSprite(load_image("left_player_stop.png"), 1, 1, gg_sprite_x, gg_sprite_y, sprites, 15)
    game(walls, floor, wall_1, wall_2, wall_3, wall_4, chest, gg_right, gg_left, gg_sprite, gg_stop_r, gg_stop_l,
         'lvl3', el=None, gerl=None, npc=None, npc_boss=npc_boss)


def game(walls, floor, wall_1, wall_2, wall_3, wall_4, chest, gg_right, gg_left, gg_sprite, gg_stop_r, gg_stop_l, lvl,
         el=None, gerl=None, npc=None, npc_boss=None):
    move_right = False
    move_left = False
    move_up = False
    move_down = False
    text1 = False
    text4 = False
    text11 = False
    text21 = False
    direction = 2
    enter_press = False
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
                    if lvl == 'lvl1':
                        if not text4:
                            sprites_note.add(scroll_npc)
                            text4 = True
                        else:
                            sprites_note.remove(scroll_npc)
                            text4 = False
                            return
                    else:
                        if not text21:
                            sprites_note.add(scroll_npc2)
                            text21 = True
                        else:
                            sprites_note.remove(scroll_npc2)
                            text21 = False
                            return
            if event.type == pygame.KEYUP and event.key == pygame.K_f:
                if f_press:
                    if lvl == 'lvl1':
                        if not text1:
                            sprites_note.add(scroll)
                            text1 = True
                        else:
                            sprites_note.remove(scroll)
                            text1 = False
                    else:
                        if not text11:
                            sprites_note.add(scroll2)
                            text11 = True
                        else:
                            sprites_note.remove(scroll2)
                            text11 = False

            if event.type == pygame.KEYUP and event.key == pygame.K_e:
                if enter_press:
                    fighting()
                    win()
                    running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                screen_start(lvl, floor, wall_1, wall_2, wall_3, wall_4, chest, gg_left, gg_sprite, el, gerl, npc,
                             npc_boss)

        camera.update(gg_sprite, width, height)
        for sprite in all_sprites:
            camera.apply(sprite)
        if not text1 and not text11 and not text4 and not text21:
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
        if lvl != 'lvl3':
            if pygame.sprite.collide_rect(gg_stop_l, npc):
                screen.blit(text2, (350, 600))
                n_press = True
        if lvl == 'lvl3':
            if pygame.sprite.collide_rect(gg_stop_l, npc_boss):
                screen.blit(text5, (350, 600))
                enter_press = True
        if pygame.sprite.collide_rect(gg_stop_l, chest):
            screen.blit(text3, (350, 600))
            f_press = True
        if text1:
            sprites_note.draw(screen)
            scroll.read()
        if text11:
            sprites_note.draw(screen)
            scroll2.read()
        if text21:
            sprites_note.draw(screen)
            scroll_npc2.read()
        if text4:
            sprites_note.draw(screen)
            scroll_npc.read()
        pygame.display.update()
        pygame.display.flip()
    save(lvl, floor, wall_1, wall_2, wall_3, wall_4, chest, gg_left, gg_sprite, el, gerl, npc, npc_boss)
    pygame.quit()


def main(result):
    number, lvl, floor_x, floor_y, wall_1_x, wall_1_y, wall_2_x, wall_2_y, wall_3_x, wall_3_y, wall_4_x, \
    wall_4_y, chest_x, chest_y, gg_left_x, gg_left_y, gg_sprite_x, gg_sprite_y, el_x, el_y, gerl_x, \
    gerl_y, npc_x, npc_y, npc_boss_x, npc_boss_y = result
    if lvl == 'lvl1':
        lvl1(lvl, floor_x, floor_y, wall_1_x, wall_1_y, wall_2_x, wall_2_y, wall_3_x, wall_3_y, wall_4_x,
             wall_4_y, chest_x, chest_y, gg_left_x, gg_left_y, gg_sprite_x, gg_sprite_y, el_x, el_y, gerl_x,
             gerl_y, npc_x, npc_y, npc_boss_x, npc_boss_y)
        clean()
        lvl, floor_x, floor_y, wall_1_x, wall_1_y, wall_2_x, wall_2_y, wall_3_x, wall_3_y, wall_4_x, \
        wall_4_y, chest_x, chest_y, gg_left_x, gg_left_y, gg_sprite_x, gg_sprite_y, el_x, el_y, gerl_x, \
        gerl_y, npc_x, npc_y, npc_boss_x, npc_boss_y = [None for i in range(25)]
    if floor_x:
        if lvl == 'lvl2':
            lvl2(lvl, floor_x, floor_y, wall_1_x, wall_1_y, wall_2_x, wall_2_y, wall_3_x, wall_3_y, wall_4_x, \
                 wall_4_y, chest_x, chest_y, gg_left_x, gg_left_y, gg_sprite_x, gg_sprite_y, el_x, el_y, gerl_x, \
                 gerl_y, npc_x, npc_y, npc_boss_x, npc_boss_y)
            clean()
            lvl3()
            clean()
        if lvl == 'lvl3':
            lvl3(lvl, floor_x, floor_y, wall_1_x, wall_1_y, wall_2_x, wall_2_y, wall_3_x, wall_3_y, wall_4_x, \
                 wall_4_y, chest_x, chest_y, gg_left_x, gg_left_y, gg_sprite_x, gg_sprite_y, el_x, el_y, gerl_x, \
                 gerl_y, npc_x, npc_y, npc_boss_x, npc_boss_y)
            clean()

    else:
        lvl2()
        clean()
        lvl3()
        clean()


def clean():
    all_sprites.empty()
    sprites.empty()
    sprites_note.empty()
