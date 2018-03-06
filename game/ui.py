import curses

from .enums import UiCell


class Ui:

    def __init__(self, game_state):
        self.game_state = game_state
        self.main = curses.initscr()
        self.game_win = curses.newwin(game_state.grid.line_num + 2, game_state.grid.col_num * 2 + 3, 1, 2)

        self.__init_colors__()
        self.main.clear()

    def step(self):
        self.main.refresh()
        self.render_grid()
        self.render_borders()
        self.game_win.refresh()

    def render_borders(self):
        grid = self.game_state.grid
        for i in range(grid.col_num * 2 + 1):
            self.game_win.addstr(0, i, ' ', curses.color_pair(UiCell.BORDER))
            self.game_win.addstr(grid.line_num + 1, i, ' ', curses.color_pair(UiCell.BORDER))

        for j in range(grid.line_num + 2):
            self.game_win.addstr(j, 0, ' ', curses.color_pair(UiCell.BORDER))
            self.game_win.addstr(j, grid.col_num * 2 + 1, ' ', curses.color_pair(UiCell.BORDER))

    def render_grid(self):
        grid = self.game_state.grid
        for i in range(grid.line_num):
            for j in range(grid.col_num):
                grid_value = grid.matrix[i, j]
                cell_color = UiCell.EMPTY
                if grid_value < 0:
                    cell_color = UiCell.APPLE
                elif grid_value > 0:
                    cell_color = UiCell.SNAKE

                self.game_win.addstr(i + 1, j * 2 + 1, '  ', curses.color_pair(cell_color))

    def close(self):
        curses.endwin()

    @staticmethod
    def __init_colors__():
        curses.start_color()
        curses.use_default_colors()
        curses.init_pair(UiCell.APPLE, curses.COLOR_RED, curses.COLOR_RED)
        curses.init_pair(UiCell.SNAKE, curses.COLOR_GREEN, curses.COLOR_GREEN)
        curses.init_pair(UiCell.BORDER, curses.COLOR_BLACK, curses.COLOR_BLACK)
