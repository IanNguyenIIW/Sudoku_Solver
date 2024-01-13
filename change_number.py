import pygame, os
from state import *
from util import *
from board import *


class Change(State):
    def __init__(self, game, board, box, solved):
        State.__init__(self, game)
        self.board = board
        self.box = box
        self.solved = solved
    def update(self, actions):
        if actions['rightMouse']:
            if self.box.holdNum != 0:
                print("hello")
                if self.box.holdNum == self.solved.val:
                    self.box.permanent = True
                    self.box.val = self.box.holdNum
                else:
                    self.board.current -= 1
                    self.box.holdNum = 0
            self.exit_state()
        if actions['escape']:
            self.board.boxes[self.box.row][self.box.col].holdNum = 0
            self.exit_state()
        if not self.box.permanent:
            if actions['one']:
                self.board.boxes[self.box.row][self.box.col].holdNum = 1
            if actions['two']:
                self.board.boxes[self.box.row][self.box.col].holdNum = 2
            if actions['three']:
                self.board.boxes[self.box.row][self.box.col].holdNum = 3
            if actions['four']:
                self.board.boxes[self.box.row][self.box.col].holdNum = 4
            if actions['five']:
                self.board.boxes[self.box.row][self.box.col].holdNum = 5
            if actions['six']:
                self.board.boxes[self.box.row][self.box.col].holdNum = 6
            if actions['seven']:
                self.board.boxes[self.box.row][self.box.col].holdNum = 7
            if actions['eight']:
                self.board.boxes[self.box.row][self.box.col].holdNum = 8
            if actions['nine']:
                self.board.boxes[self.box.row][self.box.col].holdNum = 9


        self.game.reset_keys()
    def render(self, display):
        display.fill(white)

        self.board.render(display, False, True, True)

