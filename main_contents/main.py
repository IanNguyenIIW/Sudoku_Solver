import pygame
import sys
from board import *
from util import *
from title import *

class Game:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((640,640))

        self.state_stack = []
        self.actions = {'leftMouse' : False, 'rightMouse' : False, 'one' : False,
                        'two' : False, 'three' : False, 'four' : False, 'five' : False, 'six' : False,
                        'seven' : False, 'eight' : False, 'nine' : False,
                        'escape' : False,
                        'space' : False}
        self.playing , self.running = True, True
        self.clock = pygame.time.Clock()
        self.load_states()
    def game_loop(self):
        while self.playing:
            self.get_events()
            self.update()
            self.render()

    def get_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                self.playing = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.actions['leftMouse'] = True
                if event.button == 3:
                    self.actions['rightMouse'] = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    self.actions['one'] = True
                if event.key == pygame.K_2:
                    self.actions['two'] = True
                if event.key == pygame.K_3:
                    self.actions['three'] = True
                if event.key == pygame.K_4:
                    self.actions['four'] = True
                if event.key == pygame.K_5:
                    self.actions['five'] = True
                if event.key == pygame.K_6:
                    self.actions['six'] = True
                if event.key == pygame.K_7:
                    self.actions['seven'] = True
                if event.key == pygame.K_8:
                    self.actions['eight'] = True
                if event.key == pygame.K_9:
                    self.actions['nine'] = True
                if event.key == pygame.K_ESCAPE:
                    self.actions['escape'] = True
                if event.key == pygame.K_SPACE:
                    self.actions['space'] = True
    def update(self):
        self.state_stack[-1].update(self.actions)
    def render(self):
        # click = False
        # mx, my = pygame.mouse.get_pos()
        # self.screen.fill(white)
        # self.board.check_collision((mx, my))
        # self.board.render(self.screen)
        # pygame.display.update()

        self.state_stack[-1].render(self.screen)
        pygame.display.update()
        self.clock.tick(60)
    def reset_keys(self):
        for action in self.actions:
            self.actions[action] = False

    def load_states(self):
        self.title_screen = Title(self)
        self.state_stack.append(self.title_screen)
if __name__ == "__main__":
    g = Game()
    while g.running:
        g.game_loop()