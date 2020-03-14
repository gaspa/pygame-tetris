#!/usr/bin/env python
import random

shapes = [[[1, 1],
           [1, 1]],
          [[1, 1, 0],
           [0, 1, 1]],
          [[0, 1, 1],
           [1, 1, 0]],
          [[1, 1, 1, 1]],
          [[1, 1, 1],
           [0, 1, 0]],
          [[1, 0, 0],
           [1, 1, 1]],
          [[0, 0, 1],
           [1, 1, 1]]
          ]


class Piece(object):
    def __init__(self):
        self.shape = self._generate_shape()
        self.position = (0, 0)

    @staticmethod
    def _generate_shape():
        random_shape = random.randrange(0, len(shapes))
        return shapes[random_shape]

    @property
    def row(self):
        return self.position[0]

    @property
    def column(self):
        return self.position[1]

    @property
    def width(self):
        return len(self.shape[0])

    def rotate(self):
        self.shape = [[self.shape[y][x]
                       for y in range(len(self.shape))]
                      for x in range(len(self.shape[0]) - 1, -1, -1)]


class Board(object):
    rows, cols = size = (16, 10)

    def __init__(self):
        self.landed = [[0] * Board.cols for x in range(Board.rows)]
        self.pieces = []
        self.started = False
        self.game_over = False

    def add_piece(self):
        piece = Piece()
        piece.position = (0, Board.cols // 2)
        self.pieces.append(piece)

    def move_piece_left(self):
        for piece in self.pieces:
            if piece.position[1] > 0:
                new_position = (piece.position[0], piece.position[1] - 1)
                if not self._check_collision(new_position, piece.shape):
                    piece.position = new_position

    def move_piece_right(self):
        for piece in self.pieces:
            if piece.position[1] + piece.width < Board.cols:
                new_position = (piece.position[0], piece.position[1] + 1)
                if not self._check_collision(new_position, piece.shape):
                    piece.position = new_position

    def drop_piece(self):
        for piece in self.pieces:
            while True:
                new_position = (piece.position[0] + 1, piece.position[1])
                if self._check_collision(new_position, piece.shape):
                    break
                piece.position = new_position


    def next(self):
        for piece in self.pieces:
            new_position = (piece.position[0] + 1, piece.position[1])
            if not self._check_collision(new_position, piece.shape):
                piece.position = new_position
            elif piece.position[0] == 0:
                self.game_over = True
            else:
                self._update_landed(piece.position, piece.shape)
                self._remove_piece(piece)
                self.add_piece()
        self._prune_full_lines()

    def _check_collision(self, position, shape):
        for row, shape_row in enumerate(shape):
            if (position[0] + row) >= Board.rows:
                return True
            for column, shape_value in enumerate(shape_row):
                if shape_value and self.landed[position[0] + row][position[1] + column]:
                    return True
        return False

    def _update_landed(self, position, shape):
        for row, shape_row in enumerate(shape):
            for column, shape_value in enumerate(shape_row):
                if shape_value:
                    self.landed[position[0] + row][position[1] + column] = 1

    def _remove_piece(self, piece):
        self.pieces.remove(piece)

    def _prune_full_lines(self):
        for row in self.landed:
            if all(row):
                self.landed.remove(row)
                self.landed.insert(0, [0] * Board.cols)

