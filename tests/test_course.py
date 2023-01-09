import math

import pytest

from nvgr import Course


def test_init():
    c = Course()

    assert c.degrees == 0.0
    assert str(c) == "000.0°"


def test_init_361a():
    with pytest.raises(ValueError):
        Course(361.0)


def test_init_361b():
    with pytest.raises(ValueError):
        c = Course()
        c.degrees = 361.0


def test_init_1a():
    with pytest.raises(ValueError):
        Course(-1.0)


def test_init_1b():
    with pytest.raises(ValueError):
        c = Course()
        c.degrees = -1.0


def test_north():
    c = Course(0.0)

    assert c.degrees == 0.0
    assert c.radians == 0.0
    assert str(c) == "000.0°"


def test_east():
    c = Course(90.0)

    assert c.degrees == 90.0
    assert c.radians == math.pi / 2
    assert str(c) == "090.0°"


def test_south():
    c = Course(180.0)

    assert c.degrees == 180.0
    assert c.radians == math.pi
    assert str(c) == "180.0°"


def test_west():
    c = Course(270.0)

    assert c.degrees == 270.0
    assert c.radians == math.pi * 3 / 2
    assert str(c) == "270.0°"
