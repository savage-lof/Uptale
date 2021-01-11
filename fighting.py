import pygame
import random

width, height = 1600, 900

horizontal_border_size = 350
horizontal_borders_sprites = pygame.sprite.Group()

vertical_border_size = 350
vertical_borders_sprites = pygame.sprite.Group()

border_left_x = (width / 2 - horizontal_border_size / 2) - 1
border_top_y = (height / 2 + 50) - 1
border_right_x = border_left_x + horizontal_border_size + 1
border_bottom_y = border_top_y + vertical_border_size + 1

player_sprite = pygame.sprite.Group()
blinking_sprites = pygame.sprite.Group()
killer_sprites = pygame.sprite.Group()
idle_enemy_sprites = pygame.sprite.Group()
attack_enemy_sprites = pygame.sprite.Group()
hud_sprites = pygame.sprite.Group()
timer_sprites = pygame.sprite.Group()

MYEVENTTYPE = pygame.USEREVENT + 1


def attack_1():
    Blinking(border_left_x + 1, border_top_y + 1, 100, 350)
    Blinking(border_right_x - 100, border_top_y + 1, 100, 350)


def attack_2():
    Blinking(border_left_x + 1, border_top_y + 1, 350, 50)
    Blinking(border_left_x + 1, border_top_y + 151, 350, 50)
    Blinking(border_left_x + 1, border_bottom_y - 50, 350, 50)


def attack_3():
    Blinking(border_left_x + 1, border_top_y + 1, 350, 300)
    Blinking(border_left_x + 1, border_top_y + 301, 300, 50)


def attack_4():
    Blinking(border_left_x + 1, border_top_y + 1, 350, 110)
    Blinking(border_left_x + 1, border_bottom_y - 110, 350, 110)


def attack_5():
    Blinking(border_left_x + 1, border_top_y + 1, 350, 300)
    Blinking(border_left_x + 51, border_top_y + 301, 300, 50)


def attack_6():
    Blinking(border_left_x + 1, border_top_y + 1, 145, 350)
    Blinking(border_right_x - 145, border_top_y + 1, 145, 350)
    Blinking(border_left_x + 1, border_top_y + 1, 350, 145)
    Blinking(border_left_x + 1, border_bottom_y - 145, 350, 145)


def teardown(soundObj):
    pygame.time.set_timer(MYEVENTTYPE, 0)
    soundObj.stop()
    pygame.mixer.music.stop()

    player_sprite.empty()
    vertical_borders_sprites.empty()
    horizontal_borders_sprites.empty()
    blinking_sprites.empty()
    killer_sprites.empty()


class Player(pygame.sprite.Sprite):
    image = pygame.image.load('data/swords.png')

    def __init__(self, x, y, speed, font):
        super().__init__(player_sprite)
        pygame.mixer.music.load('data/intro.mid')
        pygame.mixer.music.play()
        self.width = 30
        self.height = 30
        self.speed = speed
        self.islive = True
        self.hp = 100
        self.textsurface = font.render(str(self.hp), False, (255, 255, 255))
        self.image = Player.image
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        #  self.image = pygame.Surface((self.width, self.width), pygame.SRCALPHA, 32)
        #  pygame.draw.rect(self.image, pygame.Color('blue'), (0, 0, self.width, self.width))
        self.rect = pygame.Rect(x, y, self.width, self.width)

    def move(self, dx, dy):
        if not self.islive:
            return
        if pygame.sprite.spritecollideany(self, vertical_borders_sprites) or \
                pygame.sprite.spritecollideany(self, horizontal_borders_sprites):
            return
        self.rect.x += dx
        self.rect.y += dy
        if pygame.sprite.spritecollideany(self, vertical_borders_sprites) or \
                pygame.sprite.spritecollideany(self, horizontal_borders_sprites):
            self.rect.x -= dx
            self.rect.y -= dy

    def update(self, font):
        if not self.islive:
            return
        if pygame.sprite.spritecollideany(self, killer_sprites):
            self.hp -= 0.5
            if self.hp < 0:
                self.hp = 0
                self.islive = False
            self.textsurface = font.render(str(int(self.hp)), False, (255, 255, 255))


class HealthBar(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(hud_sprites)
        self.image = pygame.Surface((200, 40), pygame.SRCALPHA, 32)
        pygame.draw.rect(self.image, pygame.Color('green'),
                         (0, 0, 200, 40))
        self.rect = pygame.Rect(50, 50, 200, 40)

    def update(self, hp):
        self.image = pygame.transform.scale(self.image, (int(hp * 2), 40))
        r = int(-2.55 * hp + 255)
        g = 255 - r
        pygame.draw.rect(self.image, pygame.Color((r, g, 0)), (0, 0, int(hp * 2), 40))


class Border(pygame.sprite.Sprite):
    def __init__(self, x1, y1, x2, y2):
        if x1 == x2:
            super().__init__(vertical_borders_sprites)
            self.image = pygame.Surface((1, y2 - y1))
            pygame.draw.rect(self.image, pygame.Color('white'),
                             (0, 0, 1, y2 - y1))
            self.rect = pygame.Rect(x1, y1, 1, y2 - y1)
        else:
            super().__init__(horizontal_borders_sprites)
            self.image = pygame.Surface((x2 - x1, 1))
            pygame.draw.rect(self.image, pygame.Color('white'),
                             (0, 0, x2 - x1, 1))
            self.rect = pygame.Rect(x1, y1, x2 - x1, 1)


class Killer(pygame.sprite.Sprite):
    def __init__(self, rect):
        super().__init__(killer_sprites)
        self.image = pygame.Surface((rect.w, rect.h), pygame.SRCALPHA, 32)
        pygame.draw.rect(self.image, pygame.Color('red'),
                         (0, 0, rect.w, rect.h))
        self.seconds_of_life = 3
        self.rect = pygame.Rect(rect)

    def update(self, dt):
        self.seconds_of_life -= dt
        if self.seconds_of_life <= 0:
            killer_sprites.remove(self)


class Blinking(pygame.sprite.Sprite):
    def __init__(self, x1, y1, w, h):
        super().__init__(blinking_sprites)
        self.current_time = pygame.time.get_ticks()
        self.seconds_of_living = 1
        self.iswhite = True
        self.image = pygame.Surface((w, h), pygame.SRCALPHA, 32)
        self.count_of_blinking = 0
        pygame.draw.rect(self.image, pygame.Color('red'),
                         (0, 0, w, h))
        self.rect = pygame.Rect(x1, y1, w, h)

    def update(self, sound):
        if self.count_of_blinking == 8:
            sound.stop()
            blinking_sprites.remove(self)
            Killer(self.rect)
        current_time = pygame.time.get_ticks()

        delay = 150

        if current_time >= self.current_time + delay:
            self.iswhite = not self.iswhite
            if self.iswhite:
                self.image.fill(pygame.Color('red'))
            else:
                self.image.fill(pygame.Color('black'))
            self.current_time = current_time
            self.count_of_blinking += 1


class AnimatedSprite(pygame.sprite.Sprite):
    def __init__(self, sheet, columns, rows, x, y, attack):
        if attack:
            super().__init__(attack_enemy_sprites)
        else:
            super().__init__(idle_enemy_sprites)
        self.frames = []
        self.cut_sheet(sheet, columns, rows)
        self.cur_frame = 0
        self.cur_time = 0
        self.image = self.frames[self.cur_frame]
        self.rect = self.rect.move(x, y)

    def cut_sheet(self, sheet, columns, rows):
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns,
                                sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pygame.Rect(
                    frame_location, self.rect.size)))

    def update(self, dt):
        self.cur_time += dt
        if self.cur_time > 0.1:
            self.cur_frame = (self.cur_frame + 1) % len(self.frames)
            self.image = self.frames[self.cur_frame]
            self.cur_time -= 0.1


class TimerOfGame(pygame.sprite.Sprite):
    def __init__(self, font):
        super().__init__(timer_sprites)
        self.cur_time = 61
        self.font = font
        self.textsurface = self.font.render(str(int(self.cur_time)), False, (255, 255, 255))

    def update(self, dt):
        self.cur_time -= dt
        if self.cur_time < 0:
            self.cur_time = 0
        self.textsurface = self.font.render(str(int(self.cur_time)), False, (255, 255, 255))


def internal_fighting():
    screen = pygame.display.set_mode((width, height))

    FPS = 60
    soundObj = pygame.mixer.Sound('data/alarm.wav')
    gamefont = pygame.font.SysFont('Comic Sans MS', 30)

    attacks = [attack_1, attack_2, attack_3, attack_4, attack_5, attack_6]

    pygame.time.set_timer(MYEVENTTYPE, 3000)

    Border(border_left_x,
           border_top_y,
           border_right_x,
           border_bottom_y)

    Border(border_left_x,
           border_bottom_y,
           border_right_x,
           border_bottom_y)

    Border(border_left_x,
           border_top_y,
           border_left_x,
           border_bottom_y)

    Border(border_right_x,
           border_top_y,
           border_right_x,
           border_bottom_y)

    dt = 0
    clock = pygame.time.Clock()

    idle_enemy = AnimatedSprite(pygame.image.load('data/npc.png'), 11, 1, border_left_x + 75,
                                border_top_y - 200, False)
    attack_enemy = AnimatedSprite(pygame.image.load('data/npc_attack.png'), 17, 1,
                                  border_left_x + 75, border_top_y - 200, True)
    player = Player(border_right_x - horizontal_border_size / 2,
                    border_bottom_y - vertical_border_size / 2, 300, gamefont)
    gt = TimerOfGame(gamefont)
    hb = HealthBar()

    pressed_keys = {"left": False, "right": False, "up": False, "down": False}

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                teardown(soundObj)
                return False
            elif event.type == MYEVENTTYPE:
                soundObj.play()
                if not attacks:
                    attacks = [attack_1, attack_2, attack_3, attack_4, attack_5, attack_6]
                attack = random.choice(attacks)
                attack()
                attacks.remove(attack)
                pygame.time.set_timer(MYEVENTTYPE, random.randint(5000, 7000))

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    pressed_keys["left"] = True
                if event.key == pygame.K_RIGHT:
                    pressed_keys["right"] = True
                if event.key == pygame.K_UP:
                    pressed_keys["up"] = True
                if event.key == pygame.K_DOWN:
                    pressed_keys["down"] = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    pressed_keys["left"] = False
                if event.key == pygame.K_RIGHT:
                    pressed_keys["right"] = False
                if event.key == pygame.K_UP:
                    pressed_keys["up"] = False
                if event.key == pygame.K_DOWN:
                    pressed_keys["down"] = False

        tomove = player.speed / FPS
        if pressed_keys["left"]:
            player.move(-tomove, 0)
        if pressed_keys["right"]:
            player.move(tomove, 0)
        if pressed_keys["up"]:
            player.move(0, -tomove)
        if pressed_keys["down"]:
            player.move(0, tomove)

        if not player.islive:
            teardown(soundObj)
            return False

        if gt.cur_time == 0:
            return True

        screen.fill(pygame.Color('black'))
        blinking_sprites.update(soundObj)
        killer_sprites.update(dt)
        idle_enemy_sprites.update(dt)
        attack_enemy_sprites.update(dt)
        hud_sprites.update(player.hp)
        timer_sprites.update(dt)
        player_sprite.update(gamefont)

        vertical_borders_sprites.draw(screen)
        horizontal_borders_sprites.draw(screen)
        blinking_sprites.draw(screen)
        killer_sprites.draw(screen)
        if killer_sprites:
            attack_enemy_sprites.draw(screen)
        else:
            idle_enemy_sprites.draw(screen)
        hud_sprites.draw(screen)
        player_sprite.draw(screen)

        screen.blit(player.textsurface, (100, 0))
        screen.blit(gt.textsurface, (1300, 0))

        dt = clock.tick(FPS) / 1000
        pygame.display.flip()


class Dead(pygame.sprite.Sprite):
    image = pygame.image.load('data/dead.png')

    def __init__(self, *group):
        super().__init__(*group)
        self.image = Dead.image
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()
        print(self.rect)
        self.x = -self.rect.width
        self.rect.x = -self.rect.width
        self.rect.y = 0
        self.speed = 1200

    def update(self, fps):
        if self.x + self.rect.width >= width:
            return
        self.x += self.speed / fps
        self.x = min(self.x, 0)
        self.rect.x = self.x


def dead():
    all_sprites = pygame.sprite.Group()
    vehicle = Dead(all_sprites)
    screen = pygame.display.set_mode((width, height))

    fps = 60
    clock = pygame.time.Clock()
    running = True
    want_play = None

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                want_play = False
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                want_play = True
                running = False

        screen.fill(pygame.Color('black'))
        all_sprites.draw(screen)
        vehicle.update(fps)
        clock.tick(fps)
        pygame.display.flip()
    return want_play


def fighting():
    while True:
        finished = internal_fighting()
        if finished:
            return True
        want_play = dead()
        if not want_play and want_play is not None:
            break
    return False
