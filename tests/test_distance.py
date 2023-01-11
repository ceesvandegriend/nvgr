import math

import pytest

from nvgr import Distance


def test_init():
    d = Distance()

    assert d.nautical_miles == 0.0
    assert d.degrees == 0.0
    assert d.radians == 0.0
    assert str(d) == "0.0'"


def test_60NM():
    d = Distance(60.0)

    assert d.nautical_miles == 60.0
    assert d.degrees == 1.0
    assert d.radians == math.pi / 180
    assert str(d) == "60.0'"


def test_120NMa():
    d = Distance(120.0)

    assert d.nautical_miles == 120.0
    assert d.degrees == 2.0
    assert d.radians == math.pi * 2 / 180
    assert str(d) == "120.0'"


def test_120NMb():
    d = Distance()
    d.nautical_miles = 120.0

    assert d.nautical_miles == 120.0
    assert d.degrees == 2.0
    assert d.radians == math.pi * 2 / 180
    assert str(d) == "120.0'"


def test_120NMc():
    d = Distance()
    d.degrees = 2.0

    assert d.nautical_miles == 120.0
    assert d.degrees == 2.0
    assert d.radians == math.pi * 2 / 180
    assert str(d) == "120.0'"


def test_1NMa():
    with pytest.raises(ValueError):
        Distance(-1)


def test_1NMb():
    with pytest.raises(ValueError):
        d = Distance()
        d.nautical_miles = -1.0


def test_1NMc():
    with pytest.raises(ValueError):
        d = Distance()
        d.degrees = -1.0
