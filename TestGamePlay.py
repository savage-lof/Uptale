import pygame
import os
import sys

size = width, height = 1700, 900
screen = pygame.display.set_mode(size)
all_sprites = pygame.sprite.Group()


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
        width, height = self.image.get_size()
        self.image = pygame.transform.scale(self.image, (width * 2, height * 2))
        self.rect = self.image.get_rect(
            center=(850, 450))


floor = Floor()


class Wall(pygame.sprite.Sprite):

    def __init__(self, filename, center):
        image = load_image(filename, -1)
        super().__init__(all_sprites)
        self.image = image
        width, height = self.image.get_size()
        self.image = pygame.transform.scale(self.image, (width * 2, height * 2))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(
            center=center)


up_wall = Wall('up_wall.png', (850, 450 - 378))
dawn_wall = Wall('dawn_wall.png', (850, 450 + 310))
left_wall = Wall('side_wall.png', (850 - 240, 450 - 100))
right_wall = Wall('side_wall.png', (850 + 240, 450 - 100))


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

    if move_right:
        gg_sprite.rect.x += s

    if move_down:
        gg_sprite.rect.y += s

    if move_up:
        gg_sprite.rect.y -= s

    if pygame.sprite.collide_mask(gg_sprite, up_wall):
        gg_sprite.rect.y += s

    if pygame.sprite.collide_mask(gg_sprite, dawn_wall):
        gg_sprite.rect.y -= s

    if pygame.sprite.collide_mask(gg_sprite, left_wall):
        gg_sprite.rect.x += s

    if pygame.sprite.collide_mask(gg_sprite, right_wall):
        gg_sprite.rect.x -= s

    screen.fill(pygame.Color("black"))
    all_sprites.draw(screen)
    all_sprites.update()
    clock.tick(500)
    pygame.display.flip()

pygame.quit()
