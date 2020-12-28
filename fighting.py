import pygame

FPS = 60
horizontal_border_size = 600
horizontal_borders_sprites = pygame.sprite.Group()

vertical_border_size = 300
vertical_borders_sprites = pygame.sprite.Group()

player_sprite = pygame.sprite.Group()


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, speed):
        super().__init__(player_sprite)
        self.width = 25
        self.height = 25
        self.speed = speed
        self.image = pygame.Surface((self.width, self.width),
                                    pygame.SRCALPHA, 32)
        pygame.draw.rect(self.image, pygame.Color('blue'),
                         (0, 0, self.width, self.width))
        self.rect = pygame.Rect(x, y, self.width, self.width)

    def move(self, dx, dy):
        if pygame.sprite.spritecollideany(self, vertical_borders_sprites) or \
                pygame.sprite.spritecollideany(self, horizontal_borders_sprites):
            return
        self.rect.x += dx
        self.rect.y += dy
        if pygame.sprite.spritecollideany(self, vertical_borders_sprites) or \
                pygame.sprite.spritecollideany(self, horizontal_borders_sprites):
            self.rect.x -= dx
            self.rect.y -= dy


class Border(pygame.sprite.Sprite):
    def __init__(self, x1, y1, x2, y2):
        if x1 == x2:
            super().__init__(vertical_borders_sprites)
            self.image = pygame.Surface([1, y2 - y1])
            pygame.draw.rect(self.image, pygame.Color('white'),
                             (0, 0, 1, y2 - y1))
            self.rect = pygame.Rect(x1, y1, 1, y2 - y1)
        else:
            super().__init__(horizontal_borders_sprites)
            self.image = pygame.Surface([x2 - x1, 1])
            pygame.draw.rect(self.image, pygame.Color('white'),
                             (0, 0, x2 - x1, 1))
            self.rect = pygame.Rect(x1, y1, x2 - x1, 1)


def fighting():
    pygame.init()
    width, height = 1600, 900
    screen = pygame.display.set_mode((width, height))

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

        screen.fill(pygame.Color('black'))
        player_sprite.update()
        vertical_borders_sprites.draw(screen)
        horizontal_borders_sprites.draw(screen)
        player_sprite.draw(screen)
        clock.tick(FPS)
        pygame.display.flip()

    pygame.quit()
