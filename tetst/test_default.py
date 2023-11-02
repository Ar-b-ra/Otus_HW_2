import unittest

from ship import MovingObject


class MovingObjectTest(unittest.TestCase):
    def test_move_object(self):
        initial_position = (12, 5)
        velocity = (-7, 3)
        obj = MovingObject(initial_position, velocity)
        obj.move()
        self.assertEqual(obj.get_position(), (5, 8))

    def test_object_without_position(self):
        with self.assertRaises(AttributeError):
            obj = MovingObject(None, (1, 1))
            obj.move()

    def test_object_without_velocity(self):
        with self.assertRaises(AttributeError):
            obj = MovingObject((1, 1), None)
            obj.move()

    def test_object_with_immutable_position(self):
        with self.assertRaises(AttributeError):
            obj = MovingObject((1, 1), (1, 1))
            obj.position = (2, 2)
            obj.move()


if __name__ == '__main__':
    unittest.main()
