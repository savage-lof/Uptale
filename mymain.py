import pygame
from fighting import fighting
import sys

if __name__ == "__main__":
    pygame.init()
    pygame.font.init()
    if fighting():
        print('WIN')
    pygame.quit()
    sys.exit()
