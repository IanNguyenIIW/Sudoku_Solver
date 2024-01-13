import pygame

from state import State
from util import *
from sudoku_board import *
class Title(State):
    def __init__(self, game):
        State.__init__(self, game)
        self.rect = pygame.Rect(100,100,100,50)
    def update(self, actions):
        if actions['leftMouse']:
            new_state = Sudoku_board(self.game,board)
            new_state.enter_state()
        self.game.reset_keys()

    def render(self, display):
        display.fill((255,255,255))

        text = font.render("SUDOKU", True, red)

        display.blit(text, (self.rect.x, self.rect.y))
