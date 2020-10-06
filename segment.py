import pygame

from constants import SQUARE_SIZE, RED


class Segment:
    def __init__(self, row, col):
        self.row, self.col = row, col
        x = col * SQUARE_SIZE + 1
        y = row * SQUARE_SIZE + 1
        self.rect = pygame.Rect(x, y, SQUARE_SIZE - 1, SQUARE_SIZE - 1)

    def draw(self, win: pygame.Surface):
        pygame.draw.rect(win, RED, self.rect)
