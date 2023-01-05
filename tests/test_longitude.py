from nvgr import Longitude


def test_init():
    long = Longitude()

    assert long.degrees == 0.0
    assert str(long) == "000.000°"


def test_45():
    long = Longitude()
    long.degrees = 45.0

    assert long.degrees == 45.0
    assert str(long) == "045.000°"
