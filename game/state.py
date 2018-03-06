import numpy as np
import math

from .grid import GameGrid
from .enums import Direction, Cell
from .exceptions import ObstacleCollision

DEFAULT_WIDTH = 70
DEFAULT_HEIGHT = 50
DEFAULT_SNAKE_WIDTH = 3


class GameState:

    def __init__(self, width=DEFAULT_WIDTH, height=DEFAULT_HEIGHT, snake_width=DEFAULT_SNAKE_WIDTH):
        self.grid = GameGrid(height, width)
        self.grid.generate_snake(snake_width)
        self.direction = Direction.EAST
        self.grid.generate_apple()
        self.score = 0
        self.apple_base_point = math.ceil(width * height / 2)
        self.current_apple_point = self.apple_base_point

    def matrix(self):
        return np.copy(self.grid.matrix)

    def change_direction(self, direction):
        if direction is None:
            return
        direction = Direction(direction)
        if direction % 2 != self.direction % 2:
            self.direction = direction

    def step(self):
        try:
            cell = self.grid.move_snake(self.direction)
            if cell == Cell.APPLE:
                self.score += self.current_apple_point
                self.current_apple_point = self.current_apple_point
                self.grid.generate_apple()
            else:
                self.current_apple_point -= 1

                # max number of moves to get apple has been reached
                if self.current_apple_point <= 0:
                    return False

        except ObstacleCollision:
            return False
        return True

    def get_score(self):
        return self.score

    def __str__(self):
        return self.grid.__str__()
