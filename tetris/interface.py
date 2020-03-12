#!/usr/bin/env python
import sys

import pygame

from tetris.models import Board

# globals:
(screen_width, screen_height) = screen_size = (640, 480)
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)


class Tetris(object):
    def __init__(self):
        self.board = Board()
        self.screen = None

    def init(self):
        pygame.init()
        self.screen = pygame.display.set_mode(screen_size)
        self.screen.fill(black)

    def draw_board(self):
        (block_width, block_height) = block_size = (screen_width / self.board.cols, screen_height / self.board.rows)
        block_surface = pygame.Surface(block_size)
        for row_number, row in enumerate(self.board.landed):
            for col_number, landed in enumerate(row):
                # print(f"in {row_number}-{col_number} landed is {landed}")
                position = (block_width * col_number, block_height * row_number)
                block_rect = pygame.Rect(position, block_size)
                if landed:
                    block_surface.fill(red)
                else:
                    block_surface.fill(black)
                self.screen.blit(block_surface, block_rect)

    def run_tetris(self):
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(black)
            # draw the board:
            self.draw_board()

            pygame.display.flip()
