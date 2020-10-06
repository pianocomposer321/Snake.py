import pygame

# from board import Board

from state_playing import Playing
from state_menu import Menu
from constants import BLACK, FRAMERATE


class Game:
    MENU = 0
    PLAYING = 1

    def __init__(self, win):
        self.win = win
        self.running = True

        self.states = [Menu, Playing]
        self.state_ind = Game.MENU
        self.state = self.states[self.state_ind](self)

    def draw(self):
        self.win.fill(BLACK)
        self.state.draw(self.win)
        pygame.display.update()

    def set_state(self, state):
        self.state_ind = state
        self.state = self.states[self.state_ind](self)

    def run(self):
        clock = pygame.time.Clock()
        while self.running:
            clock.tick(FRAMERATE)
            state = self.state.run(self.win)

            if state is False:
                self.running = False

            # if state == Playing.COLLIDED:
            #     self.state = Game.MENU

            self.draw()
