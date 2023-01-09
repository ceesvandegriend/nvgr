from nvgr import Course, Distance, Latitude, Longitude, Loxodrome


def test_north():
    departure = Loxodrome(Latitude(0.0), Longitude(0.0))
    distance = Distance(2700.0)
    arrival = departure.north(distance)

    assert arrival.latitude.degrees == 45.0
    assert arrival.longitude.degrees == 0.0
    assert str(arrival) == "45°00.0'N 000°00.0'E"


def test_east():
    departure = Loxodrome(Latitude(0.0), Longitude(0.0))
    distance = Distance(2700.0)
    arrival = departure.east(distance)

    assert arrival.latitude.degrees == 0.0
    assert arrival.longitude.degrees == 45.0
    assert str(arrival) == "00°00.0'N 045°00.0'E"


def test_south():
    departure = Loxodrome(Latitude(0.0), Longitude(0.0))
    distance = Distance(2700.0)
    arrival = departure.south(distance)

    assert arrival.latitude.degrees == -45.0
    assert arrival.longitude.degrees == 0.0
    assert str(arrival) == "45°00.0'S 000°00.0'E"


def test_west():
    departure = Loxodrome(Latitude(0.0), Longitude(0.0))
    distance = Distance(2700.0)
    arrival = departure.west(distance)

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
    departure = Loxodrome(lat0, lng0)
    course = Course(139.0)
    distance = Distance(6.5)

    arrival = departure.dr(course, distance)

    assert str(arrival) == "46°06.9'N 006°14.0'W"
