from dataclasses import dataclass
import math


@dataclass
class Distance:
    """Distance in Nautical Miles"""

    def __init__(self, nm: float = 0.0):
        self.nautical_miles = nm

    @property
    def nautical_miles(self):
        return self._nautical_miles

    @nautical_miles.setter
    def nautical_miles(self, nm: float):
        if nm >= 0:
            self._nautical_miles = nm
        else:
            raise ValueError(nm)

    @property
    def degrees(self):
        return self._nautical_miles / 60

    @degrees.setter
    def degrees(self, deg: float):
        if deg >= 0:
            self._nautical_miles = deg * 60
        else:
            raise ValueError(deg)

    @property
    def radians(self):
        return math.radians(self._nautical_miles / 60)

    def __repr__(self):
        nm = self._nautical_miles
        return f"{nm:0.1f}NM"
