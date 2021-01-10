import pygame
from fighting import fighting
from gameover import over
import sys

if __name__ == "__main__":
    pygame.init()
    pygame.font.init()
    fighting()
    pygame.quit()
    sys.exit()
