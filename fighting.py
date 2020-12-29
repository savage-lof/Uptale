import pygame
import time

FPS = 60
horizontal_border_size = 350
horizontal_borders_sprites = pygame.sprite.Group()

vertical_border_size = 350
vertical_borders_sprites = pygame.sprite.Group()

player_sprite = pygame.sprite.Group()
blinking_sprites = pygame.sprite.Group()
killer_sprites = pygame.sprite.Group()


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, speed):
        super().__init__(player_sprite)
        self.width = 25
        self.height = 25
        self.speed = speed
        self.islive = True
        self.image = pygame.Surface((self.width, self.width),
                                    pygame.SRCALPHA, 32)
        pygame.draw.rect(self.image, pygame.Color('blue'),
                         (0, 0, self.width, self.width))
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

    def update(self):
        if not self.islive:
            return
        if pygame.sprite.spritecollideany(self, killer_sprites):
            self.islive = False
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
        pygame.draw.rect(self.image, pygame.Color('white'),
                         (0, 0, rect.w, rect.h))
        self.rect = pygame.Rect(rect)


class Blinking(pygame.sprite.Sprite):
    def __init__(self, x1, y1, w, h):
        super().__init__(blinking_sprites)
        self.current_time = pygame.time.get_ticks()
        self.iswhite = True
        self.image = pygame.Surface((w, h), pygame.SRCALPHA, 32)
        self.count_of_blinking = 0
        pygame.draw.rect(self.image, pygame.Color('white'),
                         (0, 0, w, h))
        self.rect = pygame.Rect(x1, y1, w, h)

    def update(self):
        if self.count_of_blinking == 8:
            blinking_sprites.remove(self)
            Killer(self.rect)
        current_time = pygame.time.get_ticks()

        # Время мигания
        delay = 150

        if current_time >= self.current_time + delay:
            self.iswhite = not self.iswhite
            if self.iswhite:
                self.image.fill(pygame.Color('white'))
            else:
                self.image.fill(pygame.Color('black'))
            self.current_time = current_time
            self.count_of_blinking += 1


def fighting():
    width, height = 1600, 900
    screen = pygame.display.set_mode((width, height))

    #  attack = random.choice([0, 1, 2, 3, 4, 5])
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

    clock = pygame.time.Clock()
    player = Player(border_right_x - horizontal_border_size / 2,
                    border_bottom_y - vertical_border_size / 2, 300)
    pressed_keys = {"left": False, "right": False, "up": False, "down": False}

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_0:
                    Blinking(border_left_x + 1, border_top_y + 1, 100, 350)
                    Blinking(border_right_x - 100, border_top_y + 1, 100, 350)
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
            return
        screen.fill(pygame.Color('black'))
        blinking_sprites.update()
        player_sprite.update()
        vertical_borders_sprites.draw(screen)
        horizontal_borders_sprites.draw(screen)
        blinking_sprites.draw(screen)
        killer_sprites.draw(screen)
        player_sprite.draw(screen)
        clock.tick(FPS)
        pygame.display.flip()
