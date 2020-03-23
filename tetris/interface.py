#!/usr/bin/env python
import sys

import pygame

from tetris.models import Board

# globals:
(screen_width, screen_height) = screen_size = (800, 600)
white = (255, 255, 255)
gray = (128, 128, 128)
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
        self.font = pygame.font.Font(None, 36)

    def _calculate_component_positions(self):
        available_width = screen_width * 2 // 3
        block_size_w = available_width / self.board.cols
        block_size_h = screen_height / self.board.rows
        if block_size_w > block_size_h:
            # w is wider
            self.block_size = (block_size_h, block_size_h)
        else:
            self.block_size = (block_size_w, block_size_w)
        board_size = (self.block_size[0] * self.board.cols,
                      self.block_size[1] * self.board.rows)
        self.board_surface = pygame.Surface(board_size)
        board_position = (available_width - board_size[0], 0)
        self.board_rect = pygame.Rect(board_position, board_size)
        ##
        side_labels_size = (screen_width // 3, screen_height // 3)
        next_piece_position = (available_width, 0)
        self.next_piece_surface = pygame.Surface(side_labels_size)
        self.next_piece_rect = pygame.Rect(next_piece_position, side_labels_size)
        ##
        points_position = (available_width, screen_height // 3)
        self.points_surface = pygame.Surface(side_labels_size)
        self.points_rect = pygame.Rect(points_position, side_labels_size)
        ##
        level_position = (available_width, screen_height * 2 // 3)
        self.level_surface = pygame.Surface(side_labels_size)
        self.level_rect = pygame.Rect(level_position, side_labels_size)

    def draw_board(self):
        (block_width, block_height) = self.block_size
        block_surface = pygame.Surface(self.block_size)
        self.board_surface.fill(black)

        for row_number, row in enumerate(self.board.landed):
            for col_number, landed in enumerate(row):
                # print(f"in {row_number}-{col_number} landed is {landed}")
                position = (block_width * col_number, block_height * row_number)
                block_rect = pygame.Rect(position, self.block_size)
                if landed:
                    block_surface.fill(red)
                else:
                    block_surface.fill(black)
                self.board_surface.blit(block_surface, block_rect)

        for piece in self.board.pieces:
            for row_number, piece_rows in enumerate(piece.shape):
                for column_number, piece_value in enumerate(piece_rows):
                    row = piece.row + row_number
                    column = piece.column + column_number
                    position = (block_width * column, block_height * row)
                    block_rect = pygame.Rect(position, self.block_size)
                    if piece_value:
                        block_surface.fill(green)
                        self.board_surface.blit(block_surface, block_rect)
        # next_piece:
        self.next_piece_surface.fill(black)
        for row_number, piece_rows in enumerate(self.board.next_piece.shape):
            for column_number, piece_value in enumerate(piece_rows):
                row = self.board.next_piece.row + row_number
                column = self.board.next_piece.column + column_number
                position = (block_width * column, block_height * row)
                block_rect = pygame.Rect(position, self.block_size)
                if piece_value:
                    block_surface.fill(green)
                    self.next_piece_surface.blit(block_surface, block_rect)

        # points
        self.points_surface.fill(gray)
        text = self.font.render(f'Points: {self.board.points}', 1, (10, 10, 10))
        textpos = text.get_rect(centerx=self.points_surface.get_width() / 2,
                                centery=self.level_surface.get_height() / 2)
        self.points_surface.blit(text, textpos)
        # level
        self.level_surface.fill(gray)
        text = self.font.render(f'Level: {self.board.level}', 1, (10, 10, 10))
        textpos = text.get_rect(centerx=self.level_surface.get_width() / 2,
                                centery=self.level_surface.get_height() / 2)
        self.level_surface.blit(text, textpos)

        self.screen.blit(self.board_surface, self.board_rect)
        self.screen.blit(self.next_piece_surface, self.next_piece_rect)
        self.screen.blit(self.points_surface, self.points_rect)
        self.screen.blit(self.level_surface, self.level_rect)

    def run_tetris(self):
        self._calculate_component_positions()

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

            self.screen.fill(gray)
            # draw the board:
            self.draw_board()

            pygame.display.flip()
