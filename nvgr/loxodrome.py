"""Loxodrome claculations"""
import math

from nvgr import Course, Distance, Latitude, Longitude, Position


def north(departure: Position, distance: float) -> Position:
    """
    Calculate the arrival location when sailing a North course and given distance.

    :param departure: Original position
    :type Position:

    :param distance: Distance in nautical miles
    :type float:

    :return: Calculated position
    :rtype: Position
    """
    # units are degrees
    dist = Distance(distance)
    lat0 = departure.latitude
    lng0 = departure.longitude
    delta_lat = Latitude(dist.degrees)
    lat1 = lat0 + delta_lat
    lng1 = lng0
    arrival = Position(lat1, lng1)
    return arrival


def east(departure: Position, distance: Distance) -> Position:
    """
    Calculate the arrival location when sailing an East course and given distance.

    :param departure: Original position
    :type Position:

    :param distance: Distance in nautical miles
    :type float:

    :return: Calculated position
    :rtype: Position
    """
    # units are degrees
    dist = Distance(distance)
    lat0 = departure.latitude
    lng0 = departure.longitude
    delta_lng = Longitude(math.cos(lat0.radians) * dist.degrees)
    lat1 = lat0
    lng1 = lng0 + delta_lng
    arrival = Position(lat1, lng1)
    return arrival


def south(departure: Position, distance: float) -> Position:
    """
    Calculate the arrival location when sailing a South course and given distance.

    :param departure: Original position
    :type Position:

    :param distance: Distance in nautical miles
    :type float:

    :return: Calculated position
    :rtype: Position
    """
    # units are degrees
    dist = Distance(distance)
    lat0 = departure.latitude
    lng0 = departure.longitude
    delta_lat = Latitude(dist.degrees)
    lat1 = lat0 - delta_lat
    lng1 = lng0
    arrival = Position(lat1, lng1)
    return arrival


def west(departure: Position, distance: Distance) -> Position:
    """
    Calculate the arrival location when sailing an West course and given distance.

    :param departure: Original position
    :type Position:

    :param distance: Distance in nautical miles
    :type float:

    :return: Calculated position
    :rtype: Position
    """
    # units are degrees
    dist = Distance(distance)
    lat0 = departure.latitude
    lng0 = departure.longitude
    delta_lng = Longitude(math.cos(lat0.radians) * dist.degrees)
    lat1 = lat0
    lng1 = lng0 - delta_lng
    arrival = Position(lat1, lng1)
    return arrival


def dr(departure: Position, course: Course, distance: Distance) -> Position:
    """
    Dead Reckoning: calculate the arrival location for a given course and distance.

    :param departure: Original position
    :type Position:

    :param course: Course in degrees
    :type float:

    :param distance: Distance in nautical miles
    :type float:

    :return: Calculated position
    :rtype: Position
    """
    # units are degrees
    crs = Course(course)
    dist = Distance(distance)
    lat0 = departure.latitude
    lng0 = departure.longitude
    delta_lat = Latitude(math.cos(crs.radians) * dist.degrees)
    lat1 = lat0 + delta_lat
    delta_lng = Longitude(
        math.tan(crs.radians)
        * math.log(math.tan((lat1.radians / 2) + (math.pi / 4)) / math.tan((lat0.radians / 2) + (math.pi / 4)))
        * 180
        / math.pi
    )
    lng1 = lng0 + delta_lng
    arrival = Position(lat1, lng1)
    return arrival
