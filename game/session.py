import numpy as np
import asyncio
import math

from .grid import GameGrid
from .enums import Direction, Cell
from .exceptions import ObstacleCollision

DEFAULT_WIDTH = 10
DEFAULT_HEIGHT = 10
DEFAULT_SNAKE_WIDTH = 3
DEFAULT_SPEED = 20


class GameSession:

    def __init__(self, width=DEFAULT_WIDTH,
                 height=DEFAULT_HEIGHT,
                 snake_width=DEFAULT_SNAKE_WIDTH,
                 speed=DEFAULT_SPEED):
        self.grid = GameGrid(width, height)
        self.grid.generate_snake(snake_width)
        self.direction = Direction.EAST
        self.grid.generate_apple()
        self.score = 0
        self.apple_base_point = math.ceil(width * height / 2)
        self.current_apple_point = self.apple_base_point
        self.sleep_time = 1 / speed
        self.is_running = False

    def matrix(self):
        return np.copy(self.grid.matrix)

    def change_direction(self, direction):
        direction = Direction(direction)
        if direction % 2 != self.direction % 2:
            self.direction = direction

    async def run(self):
        try:
            self.is_running = True
            while True:
                cell = self.grid.move_snake(self.direction)
                if cell == Cell.APPLE:
                    self.score += self.current_apple_point
                    self.current_apple_point = self.current_apple_point
                    self.grid.generate_apple()
                else:
                    self.current_apple_point -= 1
                    if self.current_apple_point <= 0:
                        break
                await asyncio.sleep(self.sleep_time)
        except ObstacleCollision:
            pass
        self.is_running = False

    def get_score(self):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.run())
        loop.close()
        return self.score
