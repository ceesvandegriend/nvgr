from dataclasses import dataclass
import math


@dataclass
class Course:
    """Course in degrees"""

    def __init__(self, deg: float = 0.0):
        self.degrees = deg

    @property
    def degrees(self):
        return self._degrees

    @degrees.setter
    def degrees(self, deg: float):
        if deg >= 0 and deg <= 360:
            self._degrees = deg
        else:
            raise ValueError(deg)

    @property
    def radians(self):
        return math.radians(self._degrees)

    def __repr__(self):
        d = self._degrees
        return f"{d:05.1f}\u00b0"
