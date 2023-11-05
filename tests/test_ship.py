import unittest

from move import Velocity, Position
from ship import Ship


class MovingObjectTest(unittest.TestCase):
    def setUp(self):
        self.ship = Ship()

    def test_move_object(self):
        new_velocity = Velocity(-7, 3)
        self.ship.position = Position(12, 5)
        self.ship.velocity = new_velocity
        self.ship.move()
        self.assertEquals(self.ship.position, Position(5, 8))

    def test_no_velocity(self):
        with self.assertRaises(AttributeError):
            self.ship.velocity = None
            self.ship.move()

    def test_no_position(self):
        with self.assertRaises(AttributeError):
            self.ship.position = None
            self.ship.move()

    def test_no_unable_to_move(self):
        with self.assertRaises(AttributeError):
            self.ship.position = None
            self.ship.move()


if __name__ == '__main__':
    unittest.main()
