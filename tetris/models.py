#!/usr/bin/env python


class Piece(object):
    def __init__(self):
        self.shape = []
        self.position = (0, 0)


class Board(object):
    rows, cols = size = (16, 10)

    def __init__(self):
        self.landed = [[0] * Board.cols] * Board.rows
        # Test board with some landed block here and there...
        # self.landed = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #                [0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
        #                [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        #                [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        #                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #                [0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
        #                [0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
        #                [0, 0, 0, 1, 1, 0, 0, 0, 0, 0]]
        self.pieces = []
