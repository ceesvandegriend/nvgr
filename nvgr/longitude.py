import math
import re

from dataclasses import dataclass


@dataclass
class Longitude:
    """Longitude in degrees E (positive) or W (negative)"""

    def __init__(self, deg: float = 0.0):
        self.degrees = deg

    @property
    def degrees(self):
        return self._degrees

    @degrees.setter
    def degrees(self, deg: float = 0.0):
        if deg >= -180 and deg <= 180:
            self._degrees = deg
        else:
            raise ValueError(deg)

    @property
    def radians(self):
        return math.radians(self._degrees)

    def __add__(self, other):
        return Longitude(self.degrees + other.degrees)

    def __sub__(self, other):
        return Longitude(self.degrees - other.degrees)

    def __repr__(self):
        s = "E" if self._degrees >= 0.0 else "W"
        d = math.floor(abs(self._degrees))
        m = (abs(self._degrees) - d) * 60.0
        return f"{d:03.0f}\u00b0{m:04.1f}'{s}"

    @classmethod
    def parse(cls, fmt: str) -> "Longitude":
        """Parse a latitude in the format: 000-00.0E or 000-00.0W

        retruns:
          the Longitude
        """

        match = re.search("([0123456789]{3})(.+)([0123456789.]{4})(.*)([EeWw])", fmt)

        if match:
            d = float(match.group(1))
            m = float(match.group(3))
            s = match.group(5)
        else:
            raise ValueError(fmt)

        if s in ["W", "w"]:
            degrees = (d + m / 60) * -1
        else:
            degrees = d + m / 60

        lng = Longitude(degrees)
        return lng
