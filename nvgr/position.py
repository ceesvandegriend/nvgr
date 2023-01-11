from nvgr import Latitude, Longitude, formatter


class Position:
    """A position with a latitude and longitude

    Attributes
    ----------
    latitude : Latitude
        the latitude
    longitude : Longitude
        the longitude

    Methods
    -------
    __init__(latitude, longitude) - create a new position

    __str__() - resturn the position as a string

    parse(fmt) - parse the string into a position
    """

    def __init__(self, latitude: Latitude, longitude: Longitude):
        """Creates a new position

        Parameters
        ----------
        latitude : Latitude
            the latitude
        longitude : Longitude
            the longitude
        """
        self.latitude = latitude
        self.longitude = longitude

    def __str__(self):
        """Returns the position as a string

        Returns
        -------
        str : the postions
        """
        return formatter.formatPosition(self.latitude.degrees, self.longitude.degrees)

    @classmethod
    def parse(cls, fmt: str) -> "Position":
        """Parse the string into a postion

        Parameters
        ----------
        fmt : str
            the string to parse

        Returns
        -------
        Postion : the new position
        """
        lat, lng = formatter.parsePosition(fmt)
        return Position(Latitude(lat), Longitude(lng))
