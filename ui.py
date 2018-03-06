import curses


class UI:

    def __init__(self):
        self.stdscr = None
        curses.wrapper(self.run)

    def run(self, stdscr):
        self.stdscr = stdscr
        print('alo')
        begin_x = 20
        begin_y = 7
        height = 5
        width = 40
        stdscr.refresh()
        win = curses.newwin(height, width, begin_y, begin_x)
        win.addstr('alo')
        win.refresh()
        stdscr.clear()
        stdscr.getkey()
