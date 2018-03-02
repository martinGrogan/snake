import asyncio

from game.session import GameSession


def main():
    session = GameSession()
    print(session.get_score())


if __name__ == '__main__':
    main()
