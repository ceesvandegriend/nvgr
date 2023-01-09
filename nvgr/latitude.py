import math
import re

from dataclasses import dataclass


@dataclass
class Latitude:
    """The latitude in degrees N (positive) or S (negative)

    Attributes
    ----------
    degrees : float
        the latitude in degrees: -90 <= degrees <= -90

    radians : float, readonly
        the latitude in radians: -Pi/2 <= radians <= Pi/2

    Members
    -------
    __add__(other) - Add a latitude

    __sub__(other) - Subtract a latitude

    __repr__() - Returns the latitude as a string

    parse(fmt: str) - Parse a string into a latitude
    """

    def __init__(self, deg: float = 0.0):
        """Create a new latitude

        Parameters
        ----------
        deg : float, optional
            the latitude in degrees, default: 0.0
        """
        self.degrees = deg

    @property
    def degrees(self):
        """Gets the latitude in degrees

        Returns
        -------
        float
            the latitude in degrees: -90 <= degrees <= 90
        """
        return self._degrees

    @degrees.setter
    def degrees(self, deg: float):
        """Sets the latitude in degrees

        Parameters
        ----------
        deg : float
            the latitude in degrees

        Raises
        ------
            ValueError: when -90 < latitude < 90
        """
        if deg >= -90 and deg <= 90:
            self._degrees = deg
        else:
            raise ValueError(deg)

    @property
    def radians(self):
        """Gets the latitude in radians

        Returns
        -------
        float
            the latitude in radians: -Pi/2 <= radians <= Pi/2
        """
        return math.radians(self._degrees)

    def __add__(self, other):
        """Adds a latitude

        Parameters
        ----------
        other : Latitude
            the latitude to add

        Returns
        -------
        Latitude
            the new latitude
        """
        return Latitude(self.degrees + other.degrees)

    def __sub__(self, other):
        """Subtracts a latitude

        Parameters
        ----------
        other : Latitude
            the latitude to subtract

        Returns
        -------
        Latitude
            the new latitude
        """
        return Latitude(self.degrees - other.degrees)

    def __repr__(self):
        """Returns the latitude as a string

        Returns
        -------
            the latitude as a string
        """
        s = "N" if self._degrees >= 0.0 else "S"
        d = math.floor(abs(self._degrees))
        m = (abs(self._degrees) - d) * 60.0
        return f"{d:02.0f}\u00b0{m:04.1f}'{s}"

    @classmethod
    def parse(cls, fmt: str) -> "Latitude":
        """Parse a latitude in the format: 00-00.0N or 00-00.0S

        Parameters
        ----------
        fmt : str
            the string to parse into a latitude

        Returns
        -------
        Latitude :
          the new latitude
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
