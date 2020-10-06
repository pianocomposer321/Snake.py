import pygame
import random

from constants import ROWS, COLS
from segment import Segment


class Snake:
    UP = [-1, 0]
    DOWN = [1, 0]
    RIGHT = [0, 1]
    LEFT = [0, -1]

    SNAKE = 1
    WALL = 2
    FOOD = 3

    def __init__(self, directions=None):
        head = Segment(ROWS // 2, COLS // 2)
        self.segments = [head]

        if directions is None:
            self.directions = [
                [-1, 0],
                [1, 0],
                [0, 1],
                [0, -1]
            ]
        else:
            self.directions = directions

        self.direction = random.choice(self.directions)
        random.shuffle(self.direction)

        self.points = 1
        self.growing = False

    def draw(self, win: pygame.Surface):
        for segment in self.segments:
            segment.draw(win)

    def move(self):
        self.last_move = self.direction
        head = self.segments[0]
        row = head.row + self.direction[0]
        col = head.col + self.direction[1]
        self.segments.insert(0, Segment(row, col))
        if not self.growing:
            self.segments.pop()
        else:
            self.growing = False

    def handle_event(self, event: pygame.event.EventType):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if self.direction != Snake.RIGHT:
                    self.direction = Snake.LEFT
            elif event.key == pygame.K_RIGHT:
                if self.direction != Snake.LEFT:
                    self.direction = Snake.RIGHT
            elif event.key == pygame.K_UP:
                if self.direction != Snake.DOWN:
                    self.direction = Snake.UP
            elif event.key == pygame.K_DOWN:
                if self.direction != Snake.UP:
                    self.direction = Snake.DOWN

    def grow(self):
        self.growing = True

    def check_for_collisions(self, food_row, food_col):
        squares = []
        for segment in self.segments:
            squares.append((segment.row, segment.col))

        if len(squares) > len(set(squares)):
            return Snake.SNAKE

        for segment in self.segments:
            if segment.row < 0:
                return Snake.WALL
            if segment.row > ROWS - 1:
                return Snake.WALL
            if segment.col < 0:
                return Snake.WALL
            if segment.col > COLS - 1:
                return Snake.WALL

        if self.segments[0].row == food_row and self.segments[0].col == food_col:
            self.points += 1
            return Snake.FOOD

        return False
