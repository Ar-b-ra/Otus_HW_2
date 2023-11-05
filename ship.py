from move import Move, Position, Velocity
from rotate import Rotate, Direction


class Ship(Move, Rotate):
    def move(self):
        # self.rotate()
        super().move()

    def rotate(self, new_direction: Direction):
        new_coord = Velocity(5, 7)