from abs_implementation.implementation import RealVelocity, Vector, RealPosition
from abstracts.rotate import Rotate
from ship import RotatableShip

if __name__ == "__main__":
    ship_1 = RotatableShip(Vector(RealPosition(), RealVelocity()), Rotate())
    ship_2 = RotatableShip(Vector(RealPosition(1, 2), RealVelocity(7, 9)), Rotate(15))
    ship_3 = RotatableShip(Vector(RealPosition(3, 4), RealVelocity(8, 15)), Rotate(30))

    fleet = [ship_1, ship_2, ship_3]

