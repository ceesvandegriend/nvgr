from nvgr import Latitude


def test_init():
    lat = Latitude()

    assert lat.degrees == 0.0
    assert str(lat) == "00.000°"


def test_45():
    lat = Latitude()
    lat.degrees = 45.0

    assert lat.degrees == 45.0
    assert str(lat) == "45.000°"
