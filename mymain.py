import pygame
from fighting import fighting
from gameover import over
import sys

if __name__ == "__main__":
    pygame.init()
    fighting()
    over()
    pygame.quit()
    sys.exit()
