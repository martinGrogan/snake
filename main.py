from game.session import GameSession
import os
import time


def main():
    session = GameSession()
    i = 0
    while session.next():
        time.sleep(.3)
        os.system('clear')
        print(session.grid)
        i += 1
        if i & 5 == 0:
            session.change_direction((i % 4) + 1)

    print(session.get_score())


if __name__ == '__main__':
    main()
