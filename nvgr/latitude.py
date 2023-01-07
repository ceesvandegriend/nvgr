import math

from dataclasses import dataclass


@dataclass
class Latitude:
    def __init__(self, deg: float):
        self.degrees = deg

    @property
    def radians(self):
        return math.radians(self.degrees)

    def __repr__(self):
        s = "N" if self.degrees >= 0.0 else "S"
        d = math.floor(abs(self.degrees))
        m = (abs(self.degrees) - d) * 60.0
        return f"{d:02.0f}\u00b0{m:04.1f}'{s}"
