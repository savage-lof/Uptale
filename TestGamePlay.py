import pygame
import os
import sys

size = width, height = 1700, 900
screen = pygame.display.set_mode(size)
all_sprites = pygame.sprite.Group()
walls = list()


def load_image(name, color_key=None):
    fullname = os.path.join('data', name)

    if not os.path.isfile(fullname):
        sys.exit()
    image = pygame.image.load(fullname)

    if color_key is not None:
        if color_key == -1:
            color_key = image.get_at((0, 0))
        image.set_colorkey(color_key)
    else:
        image = image.convert_alpha()

    return image


class Floor(pygame.sprite.Sprite):
    image = load_image("floor.png", -1)

    def __init__(self):
        super().__init__(all_sprites)
        self.image = Floor.image
        self.image = pygame.transform.scale(self.image, (300, 300))
        self.rect = self.image.get_rect(
            center=(850, 450))


floor = Floor()


class Wall(pygame.sprite.Sprite):

    def __init__(self, filename, center, scale):
        image = load_image(filename, -1)
        super().__init__(all_sprites)
        self.image = image
        self.image = pygame.transform.scale(self.image, scale)
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(
            center=center)


walls.append((Wall('wolfv.png', (850, 600), (300, 32)), (0, -1)))
walls.append((Wall('wallg.png', (1000, 450), (32, 300)), (-1, 0)))
walls.append((Wall('wallg.png', (700, 450), (32, 300)), (1, 0)))


class Gg(pygame.sprite.Sprite):
    def __init__(self, filename):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(
            filename).convert_alpha()
        self.mask = pygame.mask.from_surface(self.image)

        self.rect = self.image.get_rect(
            center=(850, 450))


gg_sprite = pygame.sprite.Sprite()
gg_sprite_left = pygame.sprite.Sprite()
gg_sprite_right = pygame.sprite.Sprite()

gg = Gg('data/AnimOne.png')
gg_sprite.image, gg_sprite.rect, gg_sprite.mask = gg.image, gg.rect, pygame.mask.from_surface(gg.image)
gg_sprite_left.image = pygame.transform.flip(gg_sprite.image, True, False)
gg_sprite_right.image = pygame.transform.flip(gg_sprite_left.image, True, False)

all_sprites.add(gg_sprite)

fps = 144
clock = pygame.time.Clock()
s = 1

move_right = False
move_left = False
move_up = False
move_down = False

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            move_left = True
            gg_sprite.image = gg_sprite_left.image
        if event.type == pygame.KEYUP and event.key == pygame.K_LEFT:
            move_left = False

        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            move_right = True
            gg_sprite.image = gg_sprite_right.image
        if event.type == pygame.KEYUP and event.key == pygame.K_RIGHT:
            move_right = False

        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            move_up = True
        if event.type == pygame.KEYUP and event.key == pygame.K_UP:
            move_up = False

        if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            move_down = True
        if event.type == pygame.KEYUP and event.key == pygame.K_DOWN:
            move_down = False

    if move_left:
        gg_sprite.rect.x -= s
        all_sprites.add(gg_sprite)
    if move_right:
        gg_sprite.rect.x += s
        all_sprites.add(gg_sprite)
    if move_down:
        gg_sprite.rect.y += s
        all_sprites.add(gg_sprite)
    if move_up:
        gg_sprite.rect.y -= s
        all_sprites.add(gg_sprite)
    for wall in walls:
        if pygame.sprite.collide_mask(gg_sprite, wall[0]):
            gg_sprite.rect = gg_sprite.rect.move(wall[1])

    screen.fill(pygame.Color("black"))
    all_sprites.draw(screen)
    all_sprites.update()
    clock.tick(500)
    pygame.display.flip()

pygame.quit()
