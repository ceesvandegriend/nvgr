import math
import pytest

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


def test_91N():
    with pytest.raises(ValueError):
        Latitude(91)


def test_set_91N():
    with pytest.raises(ValueError):
        lat = Latitude()
        lat.degrees = 91.0


def test_91S():
    with pytest.raises(ValueError):
        Latitude(-91)


def test_set_91S():
    with pytest.raises(ValueError):
        lat = Latitude()
        lat.degrees = -91.0


def test_parse_error():
    with pytest.raises(ValueError):
        Latitude.parse("aap noot mies")


def test_parse_45N():
    lat = Latitude.parse("45°00.0'N")

    assert lat.degrees == 45.0
    assert lat.radians == math.pi / 4
    assert str(lat) == "45°00.0'N"


def test_parse_455N():
    lat = Latitude.parse("45-30.0N")

    assert lat.degrees == 45.5


def test_parse_45S():
    lat = Latitude.parse("45-00.0S")

    assert lat.degrees == -45.0
    assert lat.radians == -math.pi / 4


def test_rotterdam():
    lat = Latitude.parse("51°55.4'N")

    assert lat.degrees == pytest.approx(51.922743, 1 / 6000)


def test_add_80N():
    lat0 = Latitude(80)
    delta_lat = Latitude(20)
    lat1 = lat0 + delta_lat

    assert lat1.degrees == 80


def test_add_85S():
    lat0 = Latitude(-85)
    delta_lat = Latitude(-20)
    lat1 = lat0 + delta_lat

    assert lat1.degrees == -75
