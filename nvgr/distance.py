import math

from nvgr.format import Formatter


class Distance:
    """Distance in Nautical Miles

    1 Nautical Mile = 1,852 km
    1 Nautical Mile = 1/60 degrees latitude

    Attributes
    ----------
    nautical_miles : float
        the distance in Nautical Miles: nautical_miles >= 0

    degrees : float
        the distance in degrees: degrees >= 0

    radians : float, readonly
        the distance in radians: radians >= 0

    Members
    -------
    __str__() - the distance in degrees as a string
    """

    def __init__(self, nm: float = 0.0):
        """Create a new distance

        Parameters
        ----------
        nm : float, optional
            the distance in Nautical Miles, default: 0.0
        """

        self.nautical_miles = nm

    @property
    def nautical_miles(self):
        """Gets the distance in Nautical Miles

        Returns
        -------
        float
            the distance in Nautical Miles
        """
        return self._nautical_miles

    @nautical_miles.setter
    def nautical_miles(self, nm: float):
        """Sets the distance in Nautical Miles

        Parameters
        ----------
        nm : float
            the distance in Nautical Miles: nautical_miles >= 0

        Raises
        ------
            ValueError when nm < 0
        """
        if nm >= 0:
            self._nautical_miles = nm
        else:
            raise ValueError(nm)

    @property
    def degrees(self):
        """Gets the distance in degrees

        Returns
        -------
        float
            the distance in degrees
        """
        return self._nautical_miles / 60

    @degrees.setter
    def degrees(self, deg: float):
        """Sets the distance in degrees

        Parameters
        ----------
        deg : float
            the distance in degrees: deg >= 0

        Raises
        ------
            ValueError when deg < 0
        """
        if deg >= 0:
            self._nautical_miles = deg * 60
        else:
            raise ValueError(deg)

    @property
    def radians(self):
        """Gets the distance in radians

        Returns
        -------
        float
            the distance in radians
        """
        return math.radians(self._nautical_miles / 60)

    def __str__(self):
        """Gets the distance as a string

        Returns
        -------
        str :
            the distance in Naitical Miles as string
        """
        return Formatter.formatDistance(self.degrees)
