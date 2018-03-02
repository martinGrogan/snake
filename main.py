from game.grid import GameGrid
from game.enums import Direction


def main():
    grid = GameGrid(5, 5)
    grid.generate_snake(3)
    grid.generate_apple()
    grid.move_snake(Direction.EAST)
    print(grid.matrix)


if __name__ == '__main__':
    main()
