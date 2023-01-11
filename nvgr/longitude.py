import math

from nvgr.format import Formatter


class Longitude:
    """The longitude in degrees E (positive) or W (negative)

    Attributes
    ----------
    degrees : float
        the longitude in degrees: -180 <= degrees <= -180

    radians : float, readonly
        the longitude in radians: -Pi <= radians <= Pi

    Members
    -------
    __add__(other) - Add a longitude

    __sub__(other) - Subtract a longitude

    __str__() - Returns the longitude as a string

    parse(fmt: str) - Parse a string into a longitude
    """

    def __init__(self, deg: float = 0.0):
        """Create a new longitude

        Parameters
        ----------
        deg : float, optional
            the longitude in degrees, default: 0.0
        """
        self.degrees = deg

    @property
    def degrees(self):
        """Gets the longitude in degrees

        Returns
        -------
        float
            the longitude in degrees: -180 <= degrees <= 180
        """
        return self._degrees

    @degrees.setter
    def degrees(self, deg: float):
        """Sets the longitude in degrees

        Parameters
        ----------
        deg : float
            the longitude in degrees

        Raises
        ------
            ValueError: when -180 < longitude < 180
        """
        if deg >= -180 and deg <= 180:
            self._degrees = deg
        else:
            raise ValueError(deg)

    @property
    def radians(self):
        """Gets the longitude in radians

        Returns
        -------
        float
            the longitude in radians: -Pi <= radians <= Pi
        """
        return math.radians(self._degrees)

    def __add__(self, other):
        """Adds a longitude

        Parameters
        ----------
        other : longitude
            the longitude to add

        Returns
        -------
        Longitude
            the new longitude
        """
        lng0 = self.degrees
        delta_lng = other.degrees
        lng1 = lng0 + delta_lng

        if lng1 > 180:
            lng1 = lng1 - 360
        elif lng1 < -180:
            lng1 = lng1 + 360

        return Longitude(lng1)

    def __sub__(self, other):
        """Subtracts a longitude

        Parameters
        ----------
        other : longitude
            the longitude to add

        Returns
        -------
        Longitude
            the new longitude
        """
        return Longitude(self.degrees - other.degrees)

    def __str__(self):
        """Returns the longitude as a string

        Returns
        -------
            the longitude as a string
        """
        return Formatter.formatLongitude(self.degrees)

    @classmethod
    def parse(cls, fmt: str) -> "Longitude":
        """Parse a longitude in the format: 000-00.0E or 000-00.0W

        Parameters
        ----------
        fmt : str
            the string to parse into a longitude

        Returns
        -------
        Longitude :
          the new longitude
        """
        return Longitude(Formatter.parseLongitude(fmt))
