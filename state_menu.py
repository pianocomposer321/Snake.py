import pygame

from constants import GREEN, RED, WIDTH, HEIGHT
from state import State
from button import Button


class Menu(State):
    def __init__(self, game):

        self.game = game

        play_again_xpos = WIDTH // 5
        play_again_ypos = (HEIGHT // 5) * 4
        play_again_button = Button("Play",
                                   GREEN,
                                   self.play,
                                   xpos=play_again_xpos,
                                   ypos=play_again_ypos,
                                   show_border=True,
                                   border_color=(255, 255, 255))

        quit_xpos = (WIDTH // 5) * 4
        quit_ypos = (HEIGHT // 5) * 4
        quit_button = Button("Quit",
                             RED,
                             quit,
                             xpos=quit_xpos,
                             ypos=quit_ypos,
                             show_border=True,
                             border_color=(255, 255, 255))

        self.buttons = [play_again_button, quit_button]

    def draw(self, win: pygame.Surface):
        for button in self.buttons:
            button.draw(win)

    def on_click(self):
        for button in self.buttons:
            button.on_click()

    def play(self):
        self.game.set_state(self.game.PLAYING)

    def run(self, win: pygame.Surface):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.on_click()
        return True
