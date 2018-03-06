import time

from game.state import GameState
from game.ui import Ui


def main():
    session = GameState()
    ui = Ui(session)
    ui.step()


    time.sleep(2)

    while session.step():
        ui.step()

    print(session.get_score())
    time.sleep(1)
    ui.close()


if __name__ == '__main__':
    main()
