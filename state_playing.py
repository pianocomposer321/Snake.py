from snake import Snake
from food import Food
from state import State
from constants import (
    MOVE_TIME,
    ROWS,
    COLS,
    SQUARE_SIZE,
    WIDTH,
    HEIGHT,
    GREEN,
    WHITE
)
import pygame
pygame.font.init()


class Playing(State):
    COLLIDED = 0

    def __init__(self, game):
        self.snake = Snake()
        self.elapsed_time = pygame.time.get_ticks()
        self.game = game
        self.food = None

        self.font = pygame.font.SysFont('Arial', 14, bold=True)
        self.point_text = "Points: "

        self.spawn_food()

    def draw_grid(self, win: pygame.Surface):
        for row in range(1, ROWS):
            start_pos = (0, row * SQUARE_SIZE)
            end_pos = (WIDTH, row * SQUARE_SIZE)
            pygame.draw.line(win, GREEN, start_pos, end_pos)

        for col in range(1, COLS):
            start_pos = (col * SQUARE_SIZE, 0)
            end_pos = (col * SQUARE_SIZE, HEIGHT)
            pygame.draw.line(win, GREEN, start_pos, end_pos)

    def spawn_food(self):
        unallowed_squares = map(lambda segment: (segment.row, segment.col),
                                self.snake.segments)
        self.food = Food(unallowed_squares=unallowed_squares)

    def draw(self, win: pygame.Surface):
        self.draw_grid(win)
        self.snake.draw(win)
        self.food.draw(win)

        point_text = self.point_text + str(self.snake.points)
        text = self.font.render(point_text, True, WHITE)
        text_rect = text.get_rect()
        text_rect.right = WIDTH
        text_rect.top = 0

        win.blit(text, text_rect)

    def move(self):
        self.snake.move()

    def handle_event(self, event: pygame.event.EventType):
        self.snake.handle_event(event)

    def check_for_collisions(self):
        return self.snake.check_for_collisions(self.food.row, self.food.col)

    def run(self, win: pygame.Surface):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            self.handle_event(event)

        new_elapsed_time = pygame.time.get_ticks()
        delta_time = new_elapsed_time - self.elapsed_time

        if delta_time >= MOVE_TIME:
            self.move()
            self.elapsed_time = new_elapsed_time

        collision = self.check_for_collisions()
        if collision == Snake.WALL or collision == Snake.SNAKE:
            self.game.set_state(self.game.MENU)
        elif collision == Snake.FOOD:
            self.snake.grow()
            self.spawn_food()

        return True
