import math
import re

from dataclasses import dataclass


@dataclass
class Latitude:
    """Latitude in degrees N (positive) or S (negative)"""

    def __init__(self, deg: float = 0.0):
        self.degrees = deg

    @property
    def degrees(self):
        return self._degrees

    @degrees.setter
    def degrees(self, deg: float):
        if deg >= -90 and deg <= 90:
            self._degrees = deg
        else:
            raise ValueError(deg)

    @property
    def radians(self):
        return math.radians(self._degrees)

    def __repr__(self):
        s = "N" if self._degrees >= 0.0 else "S"
        d = math.floor(abs(self._degrees))
        m = (abs(self._degrees) - d) * 60.0
        return f"{d:02.0f}\u00b0{m:04.1f}'{s}"

    def __add__(self, other):
        return Latitude(self.degrees + other.degrees)

    def __sub__(self, other):
        return Latitude(self.degrees - other.degrees)

    @classmethod
    def parse(cls, fmt: str) -> "Latitude":
        """Parse a latitude in the format: 00-00.0N or 00-00.0S

        retruns:
          the Latitude
        """

        match = re.search("([0123456789]{2})(.+)([0123456789.]{4})(.*)([NnSs])", fmt)

        if match:
            d = float(match.group(1))
            m = float(match.group(3))
            s = match.group(5)
        else:
            raise ValueError(fmt)

        if s in ["S", "s"]:
            degrees = (d + m / 60) * -1
        else:
            degrees = d + m / 60

        lat = Latitude(degrees)
        return lat
