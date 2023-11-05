from dataclasses import dataclass


@dataclass
class Position:
    x: float = 0
    y: float = 0

    def __add__(self, other):
        return Position(self.x + other.x, self.y + other.y)

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self


@dataclass
class Velocity:
    x_velocity: int = 0
    y_velocity: int = 0


class Move:
    def __init__(self):
        self.position = Position()
        self.velocity = Velocity()

    def move(self):
        self.position = Position(self.position.x + self.velocity.x_velocity,
                                 self.position.y + self.velocity.y_velocity)
