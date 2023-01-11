"""Loxodrome claculations"""
import math

from nvgr import Course, Distance, Latitude, Longitude, Location


class Loxodrome(Location):
    def north(self, distance: Distance) -> Location:
        """
        Calculate the arrival location when sailing a North course and given distance.

        - distance: float
            Distance in Nautical Miles
        """
        # units are degrees
        lat0 = self.latitude
        lng0 = self.longitude
        delta_lat = Latitude(distance.degrees)
        lat1 = lat0 + delta_lat
        lng1 = lng0
        arrival = Location(lat1, lng1)
        return arrival

    def south(self, distance: Distance) -> Location:
        """
        Calculate the arrival location when sailing a South course and given distance.

        - distance: float
            Distance in Nautical Miles
        """
        # units are degrees
        lat0 = self.latitude
        lng0 = self.longitude
        delta_lat = Latitude(distance.degrees)
        lat1 = lat0 - delta_lat
        lng1 = lng0
        arrival = Location(lat1, lng1)
        return arrival

    def east(self, distance: Distance) -> Location:
        """
        Calculate the arrival location when sailing an East course and given distance.

        - distance: float
            Distance in Nautical Miles
        """
        # units are degrees
        lat0 = self.latitude
        lng0 = self.longitude
        delta_lng = Longitude(math.cos(lat0.radians) * distance.degrees)
        lat1 = lat0
        lng1 = lng0 + delta_lng
        arrival = Location(lat1, lng1)
        return arrival

    def west(self, distance: float) -> Location:
        """
        Calculate the arrival location when sailing West course and given distance.

        - distance: float
            Distance in Nautical Miles
        """
        # units are degrees
        lat0 = self.latitude
        lng0 = self.longitude
        delta_lng = Longitude(math.cos(lat0.radians) * distance.degrees)
        lat1 = lat0
        lng1 = lng0 - delta_lng
        arrival = Location(lat1, lng1)
        return arrival

    def dr(self, course: Course, distance: Distance) -> Location:
        """
        Dead Reckoning: calculate the arrival location for a given course and distance.

        - course: float
          Course in degrees
        - distance: float
            Distance in Nautical Miles
        """
        # units are degrees
        lat0 = self.latitude
        lng0 = self.longitude
        lat1 = lat0 + Latitude(math.cos(course.radians) * distance.degrees)
        lng1 = lng0 + Longitude(
            math.tan(course.radians)
            * math.log(math.tan((lat1.radians / 2) + (math.pi / 4)) / math.tan((lat0.radians / 2) + (math.pi / 4)))
            * 180
            / math.pi
        )
        arrival = Location(lat1, lng1)
        return arrival
