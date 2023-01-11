import math
import pytest

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


def test_181E():
    with pytest.raises(ValueError):
        Longitude(181.0)


def test_set_181E():
    with pytest.raises(ValueError):
        lng = Longitude()
        lng.degrees = 181.0


def test_181W():
    with pytest.raises(ValueError):
        Longitude(-181.0)


def test_set_91S():
    with pytest.raises(ValueError):
        lng = Longitude()
        lng.degrees = -181.0


def test_parse_error():
    with pytest.raises(ValueError):
        Longitude.parse("aap noot mies")


def test_parse_45E():
    lng = Longitude.parse("045°00.0'E")

    assert lng.degrees == 45.0
    assert lng.radians == math.pi / 4


def test_parse_455E():
    lng = Longitude.parse("045-30.0E")

    assert lng.degrees == 45.5


def test_parse_45W():
    lng = Longitude.parse("045°00.0'W")

    assert lng.degrees == -45.0
    assert lng.radians == -math.pi / 4


def test_rotterdam():
    lng = Longitude.parse("004°28.8'E")

    assert lng.degrees == pytest.approx(4.479305, 1 / 6000)


def test_add_170E():
    lng0 = Longitude(170)
    delta_lng = Longitude(20)
    lng1 = lng0 + delta_lng

    assert lng1.degrees == -170


def test_add_165W():
    lng0 = Longitude(-165)
    delta_lng = Longitude(-20)
    lng1 = lng0 + delta_lng

    assert lng1.degrees == 175
