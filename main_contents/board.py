import pygame
import sys
from util import *
from sudoku import *
class Board:
    def __init__(self, rawBoard) -> None:
        self.boxes = []
        self.rawBoard = rawBoard
        self.initialize(rawBoard)


        self.lives = 3
        self.current = 3
    def initialize(self,rawBoard):
        for i, ele in enumerate(rawBoard):
            row = []
            for j, val in enumerate(ele):
                if val == 0:
                    row.append(box(i,j, val, False))
                else:
                    row.append(box(i, j, val, True))
            self.boxes.append(row)
    def check_collision(self, mouse):
        for row in self.boxes:
            for ele in row:
                if ele.rect.collidepoint(mouse):
                    ele.hover = True

                else:
                    ele.hover = False

    def equalBoardfromgame(self):
        for i,row in enumerate(self.boxes):
            for j, ele in enumerate(row):
                self.rawBoard[i][j] = ele.val
    def equalBoardfromraw(self):
        for i,row in enumerate(self.rawBoard):
            for j, ele in enumerate(row):
                self.boxes[i][j].val = ele
    def render(self, display, g, hovering, solve):

        pygame.draw.line(display,black, (3* sideLength, 0),(3* sideLength, 9 * sideLength), 5)
        pygame.draw.line(display, black, (6 * sideLength, 0), (6 * sideLength, 9 * sideLength), 5)

        pygame.draw.line(display, black, (0, 3 * sideLength), (9 * sideLength, 3 * sideLength), 5)
        pygame.draw.line(display, black, (0,6 * sideLength), (9 * sideLength, 6 * sideLength), 5)
        pygame.draw.line(display, black, (0, 9 * sideLength), (9 * sideLength, 9 * sideLength), 5)
        for row in self.boxes:
            for ele in row:
                ele.draw(display, g, hovering, solve)
        for x in range(self.lives - self.current):
            pygame.draw.line(display,red,(0 + 5 + x * sideLength, 9 * sideLength + 5),(sideLength - 5 + x * sideLength, 9 * sideLength + sideLength - 5), 3)
            pygame.draw.line(display, red, (0 + 5 + x * sideLength, 9 * sideLength + sideLength - 5),(sideLength - 5 + x * sideLength, 9 * sideLength + 5), 3)

        text = fontdir.render('left click to select', True, black)
        text2 = fontdir.render('right click to confirm', True, black)
        text3 = fontdir.render('space to solve', True, black)
        text4 = fontdir.render('ESC to exit', True, black)
        display.blit(text, (text.get_size()[0] + 300,text.get_size()[1] - sideLength / 2 + 20))
        display.blit(text2, (text.get_size()[0] + 295, text.get_size()[1] - sideLength / 2 + 40))
        display.blit(text3, (text.get_size()[0] + 300, text.get_size()[1] - sideLength / 2 + 60))
        display.blit(text4, (text.get_size()[0] + 300, text.get_size()[1] - sideLength / 2 + 80))
class box:

    def __init__(self, row, col, val, permanent) -> None:
        self.row = row 
        self.col = col 
        self.val = val

        self.rect = self.rect()
        self.holdNum = 0
        self.hover = False
        self.permanent = permanent
    def check_collision(self, mouse):
        if self.rect.collidepoint(mouse):
            self.hover = True
        self.hover = False

    def rect(self):
        return pygame.Rect(self.col * sideLength,self.row * sideLength, sideLength, sideLength)
    
    def draw(self, display, g, hovering, solve):
        if solve:
            if not self.hover:
                pygame.draw.rect(display,black,self.rect, 1)
            else:
                pygame.draw.rect(display, blue, self.rect, 3)
        else:

            if hovering:
                if not self.hover:
                    pygame.draw.rect(display,black,self.rect, 1)
                else:
                    if g:
                        pygame.draw.rect(display, greengr, self.rect, 3)
                    else:
                        pygame.draw.rect(display, red, self.rect, 3)
                    if self.val == 0:
                        pygame.draw.rect(display, red, self.rect, 3)
        text = font.render(str(self.val), True, black)
        textHold = font.render(str(self.holdNum), True, grey)
        if self.val != 0:
            display.blit(text,(self.rect.x + text.get_size()[0], self.rect.y + text.get_size()[1] - sideLength/2))
        elif self.holdNum != 0:
            display.blit(textHold, (self.rect.x + text.get_size()[0], self.rect.y + text.get_size()[1] - sideLength / 2))

    def inputNum(self):

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    self.holdNum = 1
                if event.key == pygame.K_2:
                    self.holdNum = 2
                if event.key == pygame.K_3:
                    self.holdNum = 3
                if event.key == pygame.K_4:
                    self.holdNum = 4
                if event.key == pygame.K_5:
                    self.holdNum = 5
                if event.key == pygame.K_6:
                    self.holdNum = 6
                if event.key == pygame.K_7:
                    self.holdNum = 7
                if event.key == pygame.K_8:
                    self.holdNum = 8
                if event.key == pygame.K_9:
                    self.holdNum = 9



