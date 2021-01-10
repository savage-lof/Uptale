import pygame

FPS = 60
horizontal_border_size = 350
horizontal_borders_sprites = pygame.sprite.Group()

vertical_border_size = 350
vertical_borders_sprites = pygame.sprite.Group()

player_sprite = pygame.sprite.Group()
blinking_sprites = pygame.sprite.Group()
killer_sprites = pygame.sprite.Group()


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
            self.hp -= 1
            self.textsurface = font.render(str(self.hp), False, (255, 255, 255))
            return


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


def fighting():
    width, height = 1600, 900
    screen = pygame.display.set_mode((width, height))

    soundObj = pygame.mixer.Sound('data/alarm.wav')
    gamefont = pygame.font.SysFont('Comic Sans MS', 30)

    border_left_x = (width / 2 - horizontal_border_size / 2) - 1
    border_top_y = (height / 2 + 50) - 1
    border_right_x = border_left_x + horizontal_border_size + 1
    border_bottom_y = border_top_y + vertical_border_size + 1

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
    player = Player(border_right_x - horizontal_border_size / 2,
                    border_bottom_y - vertical_border_size / 2, 300, gamefont)
    pressed_keys = {"left": False, "right": False, "up": False, "down": False}

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                soundObj.stop()
                pygame.mixer.music.stop()
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    soundObj.play()
                    Blinking(border_left_x + 1, border_top_y + 1, 100, 350)
                    Blinking(border_right_x - 100, border_top_y + 1, 100, 350)

                if event.key == pygame.K_2:
                    soundObj.play()
                    Blinking(border_left_x + 1, border_top_y + 1, 350, 50)
                    Blinking(border_left_x + 1, border_top_y + 151, 350, 50)
                    Blinking(border_left_x + 1, border_bottom_y - 50, 350, 50)

                if event.key == pygame.K_3:
                    soundObj.play()
                    Blinking(border_left_x + 1, border_top_y + 1, 350, 300)
                    Blinking(border_left_x + 1, border_top_y + 301, 300, 50)

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
            soundObj.stop()
            pygame.mixer.music.stop()
            return
        screen.fill(pygame.Color('black'))
        blinking_sprites.update(soundObj)
        killer_sprites.update(dt)
        player_sprite.update(gamefont)

        vertical_borders_sprites.draw(screen)
        horizontal_borders_sprites.draw(screen)
        blinking_sprites.draw(screen)
        killer_sprites.draw(screen)
        player_sprite.draw(screen)

        screen.blit(player.textsurface, (100, 0))

        dt = clock.tick(FPS) / 1000
        pygame.display.flip()
