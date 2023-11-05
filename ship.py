from abs_implementation.implementation import Vector
from abs_implementation.move import Move
from abs_implementation.rotatable_move import RotatableMove
from abstracts.rotate import Rotate
from abstracts.vector import Position


class Ship(Move):
    def __init__(self, vector: Vector):
        super().__init__(vector)

    def go_to_position(self, new_position: Position):
        self.vector.set_position(new_position)


class RotatableShip(RotatableMove):
    def __init__(self, vector: Vector, rotator: Rotate):
        super().__init__(vector, rotator)

    def go_to_position(self, new_position: Position):
        self.vector.set_position(new_position)

    def rotate(self, angle):
        self.angle = angle
        self.get_new_velocity(angle, self.vector.position)
