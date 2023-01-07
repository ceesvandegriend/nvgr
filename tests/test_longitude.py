import math

from nvgr import Longitude


def test_init():
    lng = Longitude(0.0)

    assert lng.degrees == 0.0
    assert lng.radians == 0.0
    assert str(lng) == "000°00.0'E"


def test_45E():
    lng = Longitude(45.0)

    assert lng.degrees == 45.0
    assert lng.radians == math.pi / 4
    assert str(lng) == "045°00.0'E"


def test_45W():
    lng = Longitude(-45.0)

    assert lng.degrees == -45.0
    assert lng.radians == -math.pi / 4
    assert str(lng) == "045°00.0'W"
