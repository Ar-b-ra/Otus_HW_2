from abc import ABC
from dataclasses import dataclass


@dataclass
class Ship:
    x: int = 0
    y: int = 0
    velocity: (int, int) = 0, 0
    direction: float = 0  # угол, на который повёртун корабль относительно начала коордигнат


class Movable(ABC):

    def move(self, *args, **kwargs):
        pass


class Rotatable(ABC):
    def rotate(self, *args, **kwargs):
        pass
