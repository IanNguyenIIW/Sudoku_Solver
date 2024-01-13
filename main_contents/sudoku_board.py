import pygame, os
from state import *
from util import *
from board import *
from change_number import *
from sudoku import *
from util import *
import time
class Sudoku_board(State):
    def __init__(self, game,boardimp):
        State.__init__(self,game)
        self.board= Board(boardimp)
        copyboard = boardimp.copy()
        solve(copyboard)
        self.solvedBoard = Board(copyboard)


    def update(self, actions):
        mx, my = pygame.mouse.get_pos()

        for row in self.board.boxes:
            for ele in row:
                if ele.rect.collidepoint((mx,my)):
                    ele.hover = True
                    if actions['leftMouse']:
                        new_state = Change(self.game,self.board,ele,self.solvedBoard.boxes[ele.row][ele.col])
                        new_state.enter_state()

                else:
                    ele.hover = False

        if actions['space']:
            for row in self.board.boxes:
                for ele in row:
                    ele.hover = False
            self.solveGame(self.board.rawBoard)

        self.board.equalBoardfromgame()

        self.game.reset_keys()
    def render(self, display):
        display.fill(white)


        self.board.render(display,True,True ,True)

    def solveGame(self,board):

        pygame.time.delay(delay)
        find = find_empty(board)
        # base case321
        if not find:
            return True
        else:
            row, col = find
        # check the empty spot for a valid number
        for i in range(1, 10):
            if valid(board, i, (row, col)):
                board[row][col] = i
                self.board.equalBoardfromraw()

                self.board.boxes[row][col].hover = True
                self.game.screen.fill(white)
                self.board.render(self.game.screen, True, True, False)
                pygame.display.update()
                if self.solveGame(board):
                    return True



                board[row][col] = 0
                self.game.screen.fill(white)
                self.board.render(self.game.screen, False, True, False)
        return False

