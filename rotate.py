from abc import ABC
from dataclasses import dataclass


@dataclass
class Direction:
    angle: int


class Rotate(ABC):
    def rotate(self, new_direction: Direction):
        pass
