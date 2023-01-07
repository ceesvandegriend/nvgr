"""Loxodrome claculations"""
import math
from numpy import log as ln

from nvgr import Latitude, Longitude, Location


class Loxodrome(Location):
    def north(self, distance: float) -> Location:
        """
        Calculate the arrival location when sailing a North course and given distance.

        - distance: float
            Distance in Nautical Miles
        """
        # units are degrees
        lat0 = self.latitude.degrees
        lng0 = self.longitude.degrees
        delta_lat = distance / 60.0
        lat1 = lat0 + delta_lat
        lng1 = lng0
        arrival = Location(Latitude(lat1), Longitude(lng1))
        return arrival

    def south(self, distance: float) -> Location:
        """
        Calculate the arrival location when sailing a South course and given distance.

        - distance: float
            Distance in Nautical Miles
        """
        # units are degrees
        lat0 = self.latitude.degrees
        lng0 = self.longitude.degrees
        delta_lat = distance / 60.0
        lat1 = lat0 - delta_lat
        lng1 = lng0
        arrival = Location(Latitude(lat1), Longitude(lng1))
        return arrival

    def east(self, distance: float) -> Location:
        """
        Calculate the arrival location when sailing an East course and given distance.

        - distance: float
            Distance in Nautical Miles
        """
        # units are degrees
        lat0 = self.latitude.degrees
        lng0 = self.longitude.degrees
        delta_lng = math.cos(math.radians(lat0)) * distance / 60.0
        lat1 = lat0
        lng1 = lng0 + delta_lng
        arrival = Location(Latitude(lat1), Longitude(lng1))
        return arrival

    def west(self, distance: float) -> Location:
        """
        Calculate the arrival location when sailing West course and given distance.

        - distance: float
            Distance in Nautical Miles
        """
        # units are degrees
        lat0 = self.latitude.degrees
        lng0 = self.longitude.degrees
        delta_lng = math.cos(math.radians(lat0)) * distance / 60.0
        lat1 = lat0
        lng1 = lng0 - delta_lng
        arrival = Location(Latitude(lat1), Longitude(lng1))
        return arrival

    def dr(self, course: float, distance: float) -> Location:
        """
        Dead Reckoning: calculate the arrival location for a given course and distance.

        - course: float
          Course in degrees
        - distance: float
            Distance in Nautical Miles
        """
        # units are degrees
        lat0 = self.latitude.degrees
        lng0 = self.longitude.degrees
        lat1 = lat0 + math.cos(math.radians(course)) * distance / 60
        lng1 = (
            lng0
            + math.tan(math.radians(course))
            * ln(math.tan(math.radians(lat1 / 2 + math.pi / 4))
            / math.tan(math.radians(lat0 / 2 + math.pi / 4)))
            * 180.0
            / math.pi
        )
        arrival = Location(Latitude(lat1), Longitude(lng1))
        return arrival
