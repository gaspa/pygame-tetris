#!/usr/bin/env python
import sys

import pygame

from tetris.models import Board

# globals:
(screen_width, screen_height) = screen_size = (640, 480)
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)


class Tetris(object):
    def __init__(self):
        self.board = Board()
        self.screen = None
        self.board.add_piece()

    def init(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        pygame.time.set_timer(pygame.USEREVENT, 1000)
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

        for piece in self.board.pieces:
            for row_number, piece_rows in enumerate(piece.shape):
                for column_number, piece_value in enumerate(piece_rows):
                    row = piece.row + row_number
                    column = piece.column + column_number
                    position = (block_width * column, block_height * row)
                    block_rect = pygame.Rect(position, block_size)
                    if piece_value:
                        block_surface.fill(green)
                        self.screen.blit(block_surface, block_rect)

    def run_tetris(self):
        while 1:
            self.clock.tick(30)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.USEREVENT:
                    if self.board.started and not self.board.game_over:
                        self.board.next()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.board.started = True
                    if event.key == pygame.K_LEFT:
                        self.board.move_piece_left()
                    if event.key == pygame.K_RIGHT:
                        self.board.move_piece_right()
                    if event.key == pygame.K_UP:
                        self.board.pieces[0].rotate()
                    if event.key == pygame.K_DOWN:
                        self.board.drop_piece()

            self.screen.fill(black)
            # draw the board:
            self.draw_board()

            pygame.display.flip()
