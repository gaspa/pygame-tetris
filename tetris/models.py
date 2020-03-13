#!/usr/bin/env python


class Piece(object):
    def __init__(self):
        self.shape = self._generate_shape()
        self.position = (0, 0)

    @staticmethod
    def _generate_shape():
        return [[1, 1], [1, 1]]

    @property
    def row(self):
        return self.position[0]

    @property
    def column(self):
        return self.position[1]


class Board(object):
    rows, cols = size = (16, 10)

    def __init__(self):
        self.landed = [[0] * Board.cols] * Board.rows
        # Test board with some landed block here and there...
        self.landed = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
                       [0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
                       [0, 0, 0, 1, 1, 0, 0, 0, 0, 0]]
        self.pieces = []

    def add_piece(self):
        piece = Piece()
        piece.position = (0, Board.cols // 2)
        self.pieces.append(piece)

    def next(self):
        for piece in self.pieces:
            new_position = (piece.position[0] + 1, piece.position[1])
            if not self._check_collision(new_position, piece.shape):
                piece.position = new_position
            else:
                self._update_landed(piece.position, piece.shape)
                self._remove_piece(piece)
                self.add_piece()

    def _check_collision(self, position, shape):
        for row, shape_row in enumerate(shape):
            for column, shape_value in enumerate(shape_row):
                if shape_value and self.landed[position[0] + row][position[1] + column]:
                    return True
        return False

    def _update_landed(self, position, shape):
        for row, shape_row in enumerate(shape):
            for column, shape_value in enumerate(shape_row):
                self.landed[position[0] + row][position[1] + column] = shape_value

    def _remove_piece(self, piece):
        self.pieces.remove(piece)
