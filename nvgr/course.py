import math

from nvgr import formatter


class Course:
    """Course in degrees

    :attr degrees: the course in degrees: 0 <= degrees <= 360
    :type float:

    :attr radians: readonly, the course in radians: 0 <= radians <= 2 Pi
    :type float:


    Members
    -------
    __str__() - the course in degrees as a string
    """

    def __init__(self, deg: float = 0.0):
        """Create a new course

        Parameters
        ----------
        deg : float, optional
            the course in degrees, default: 0.0
        """
        self.degrees = deg

    @property
    def degrees(self):
        """Gets the course in degrees

        Returns
        -------
        float
            the course in degrees: 0 <= degrees <= 360
        """
        return self._degrees

    @degrees.setter
    def degrees(self, deg: float):
        """Sets the course in degrees

        Parameters
        ----------
        deg : float
            the course in degrees

        Raises
        ------
            ValueError: when deg < 0 or deg > 360
        """
        if deg >= 0 and deg <= 360:
            self._degrees = deg
        else:
            raise ValueError(deg)

    @property
    def radians(self):
        """Gets the course in radians

        Returns
        -------
        float :
            the course in radians: 0 <= radians <= 2 Pi
        """
        return math.radians(self._degrees)

    def __str__(self):
        """Gets the course as a string

        Returns
        -------
        str :
            the course in degrees as string
        """
        return formatter.formatCourse(self.degrees)
