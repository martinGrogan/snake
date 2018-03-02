class SizeError(ValueError):
    pass


class ObstacleCollision(IndexError):
    pass


class WallCollision(ObstacleCollision):
    pass


class SnakeCollision(ObstacleCollision):
    pass


class IllegalMovement(SnakeCollision):
    pass
