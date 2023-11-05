from abs_implementation.implementation import RealVelocity, Vector, RealPosition
from abstracts.vector import Position
from ship import Ship

if __name__ == "__main__":
    position = RealPosition()
    velocity = RealVelocity()
    vector = Vector(position, velocity)
    unmovable_ship = Ship(vector)
    unmovable_ship.move()

