import enum


@enum.unique
class Cell(enum.IntEnum):
    APPLE = -1
    EMPTY = 0


class Direction(enum.IntEnum):
    NORTH = enum.auto()
    EAST = enum.auto()
    SOUTH = enum.auto()
    WEST = enum.auto()

