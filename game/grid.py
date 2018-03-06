import numpy as np
import random
from termcolor import colored

from .exceptions import *
from .enums import Cell, Direction

MIN_SIZE = 4

BORDER = colored(' ', 'white', 'on_white')
EMPTY_CELL = '  '
APPLE_CELL = colored('  ', 'red', 'on_red')
SNAKE_CELL = colored('  ', 'green', 'on_green')


class GameGrid:

    def __init__(self, line_num, col_num):
        if line_num < MIN_SIZE or col_num < MIN_SIZE:
            raise SizeError('line and column number should be higher than %d' % MIN_SIZE)

        self.line_num = line_num
        self.col_num = col_num
        self.matrix = np.empty((line_num, col_num,), dtype=int)
        self.matrix[:] = 0

    def generate_snake(self, width):
        if width >= self.col_num:
            raise SizeError('snake base length should be less than %d' % self.col_num)
        if width < 1:
            raise SizeError('snake base length should be higher than zero')

        y = random.randint(0, self.line_num - 1)
        for i in range(width, 0, -1):
            self.matrix[y, i - 1] = i

    def generate_apple(self):
        while True:
            x = random.randint(0, self.col_num - 1)
            y = random.randint(0, self.line_num - 1)
            if self.matrix[y, x] == Cell.EMPTY:
                self.matrix[y, x] = Cell.APPLE
                break

    def move_snake(self, direction):
        direction = Direction(direction)
        pos = self.calculate_new_position(self.snake_head(), direction)
        dst = self.get_dst_cell(pos)

        if dst == self.snake_length() - 1:
            raise IllegalMovement('cannot go %s' % direction.name)
        if dst > Cell.EMPTY:
            raise SnakeCollision('hit at snake at position %d' % dst)

        self.matrix[pos] = self.snake_length() + 1

        if dst != Cell.APPLE:
            self.matrix[self.matrix > 0] -= 1

        return dst

    def snake_head(self):
        indices = np.where(self.matrix == self.matrix.max())
        return tuple(map(lambda x: x[0], indices))

    def snake_length(self):
        return self.matrix.max()

    def get_dst_cell(self, pos):
        if min(pos) < 0 or pos[0] >= self.line_num or pos[1] >= self.col_num:
            raise WallCollision('invalid point (%d, %d)' % pos)
        return self.matrix.__getitem__(pos)

    def __str__(self):
        real_width = self.col_num * 2 + 2
        view = top_border(real_width)
        for line in self.matrix:
            view += BORDER
            for cell in line:
                if cell == Cell.EMPTY:
                    view += EMPTY_CELL
                elif cell == Cell.APPLE:
                    view += APPLE_CELL
                else:
                    view += SNAKE_CELL
            view += BORDER + '\n'
        return view + bottom_border(real_width)

    @staticmethod
    def calculate_new_position(head, direction):
        Direction(direction)
        if direction == Direction.NORTH:
            return head[0] - 1, head[1]
        elif direction == Direction.EAST:
            return head[0], head[1] + 1
        elif direction == Direction.SOUTH:
            return head[0] + 1, head[1]
        elif direction == Direction.WEST:
            return head[0], head[1] - 1


def top_border(width):
    return '%s\n' % (BORDER * width)


def bottom_border(width):
    return top_border(width)
