import math

from nvgr import Latitude


def test_init():
    lat = Latitude(0.0)

    assert lat.degrees == 0.0
    assert lat.radians == 0.0
    assert str(lat) == "00°00.0'N"


def test_45N():
    lat = Latitude(45.0)

    assert lat.degrees == 45.0
    assert lat.radians == math.pi / 4
    assert str(lat) == "45°00.0'N"


def test_45S():
    lat = Latitude(-45.0)

    assert lat.degrees == -45.0
    assert lat.radians == -math.pi / 4
    assert str(lat) == "45°00.0'S"
