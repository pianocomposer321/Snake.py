from constants import WIDTH, HEIGHT, WINDOW_TITLE
from game import Game
import pygame
pygame.init()
# input()


win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(WINDOW_TITLE)
game = Game(win)
game.run()
