from abc import ABC, abstractmethod

ANGLE_STEPS = 36000


class Rotate(ABC):

    def __init__(self, init_direction):
        self.direction = init_direction

    @abstractmethod
    def rotate(self, direction):
        self.direction = direction
