from nvgr import Latitude, Longitude, Position

from nvgr.loxodrome import north, east, south, west, dr


def test_north():
    departure = Position.parse("00-00.0N 000-00.0W")
    arrival = north(departure, 2700.0)

    assert arrival.latitude.degrees == 45.0
    assert arrival.longitude.degrees == 0.0
    assert str(arrival) == "45°00.0'N 000°00.0'E"


def test_east():
    departure = Position.parse("00-00.0N 000-00.0W")
    arrival = east(departure, 2700.0)

    assert arrival.latitude.degrees == 0.0
    assert arrival.longitude.degrees == 45.0
    assert str(arrival) == "00°00.0'N 045°00.0'E"


def test_south():
    departure = Position.parse("00-00.0N 000-00.0W")
    arrival = south(departure, 2700.0)

    assert arrival.latitude.degrees == -45.0
    assert arrival.longitude.degrees == 0.0
    assert str(arrival) == "45°00.0'S 000°00.0'E"


def test_west():
    departure = Position.parse("00-00.0N 000-00.0W")
    arrival = west(departure, 2700.0)

    assert arrival.latitude.degrees == 0.0
    assert arrival.longitude.degrees == -45.0
    assert str(arrival) == "00°00.0'N 045°00.0'W"


def test_dr():
    # I've to check calculation!
    #
    # departure = 46 11.8’N 006 20.2’W
    # course = 139.0
    # distance = 6.5 NM
    lat0 = Latitude(46.19666666666666668)
    lng0 = Longitude(-6.33666666666666667)
    departure = Position(lat0, lng0)
    arrival = dr(departure, 139.0, 6.5)

    assert str(arrival) == "46°06.9'N 006°14.0'W"
