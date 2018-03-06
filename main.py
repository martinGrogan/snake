import time
import curses

from game.session import GameSession
from ui import UI


def main():
    try:
        session = GameSession()
        std = curses.initscr()
        std.clear()
        std.refresh()
        curses.start_color()

        curses.use_default_colors()

        while session.step():
            std.clear()
            curses.init_pair(1, curses.COLOR_RED, curses.COLOR_RED)
            view = session.__str__()
            std.addstr('alo', curses.color_pair(1))
            std.refresh()
            time.sleep(2)

        print(session.get_score())
    except Exception as e:
        curses.endwin()
        raise e

    curses.endwin()


if __name__ == '__main__':
    main()
