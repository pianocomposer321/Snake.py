import pygame
import random

from constants import SQUARE_SIZE, YELLOW, ROWS, COLS


class Food:
    def __init__(self, row=-1, col=-1, unallowed_squares=[]):
        if row == -1 and col == -1:
            row = random.randint(0, ROWS - 1)
            col = random.randint(0, COLS - 1)

            while (row, col) in unallowed_squares:
                row = random.randint(0, ROWS - 1)
                col = random.randint(0, COLS - 1)

        self.row, self.col = row, col
        x = col * SQUARE_SIZE + 1
        y = row * SQUARE_SIZE + 1
        self.rect = pygame.Rect(x, y, SQUARE_SIZE - 1, SQUARE_SIZE - 1)

    def draw(self, win: pygame.Surface):
        pygame.draw.rect(win, YELLOW, self.rect)
