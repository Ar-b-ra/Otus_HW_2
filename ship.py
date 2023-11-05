from abs_implementation.implementation import Vector
from abstracts.move import Move
from abstracts.rotate import Rotate
from abstracts.vector import Position


class Ship(Move, Rotate):
    def __init__(self, vector: Vector):
        super().__init__(vector)

    def go_to_position(self, new_position: Position):
        self.vector.set_position(new_position)

    def rotate(self, direction):
        pass
