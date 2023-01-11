import pytest

from nvgr import Latitude, Longitude, Position


def test_rotterdam():
    # Google Maps: Rotterdam Stadhuis: 51.922743, 4.479305
    # 51°55.4'N 004°28.8'E
    lat = Latitude(51.922743)
    lng = Longitude(4.479305)
    rotterdam = Position(lat, lng)

    assert str(rotterdam.latitude) == "51°55.4'N"
    assert str(rotterdam.longitude) == "004°28.8'E"
    assert str(rotterdam) == "51°55.4'N 004°28.8'E"


def test_parse_aap():
    with pytest.raises(ValueError):
        Position.parse("aap noot mies")


def test_parse_rotterdam():
    rotterdam = Position.parse("51°55.4'N 004°28.8'E")

    assert str(rotterdam.latitude) == "51°55.4'N"
    assert str(rotterdam.longitude) == "004°28.8'E"
    assert str(rotterdam) == "51°55.4'N 004°28.8'E"


def test_buenos_aires():
    lat = Latitude(-34.611523)
    lng = Longitude(-58.421025)
    buenos_aires = Position(lat, lng)

    assert str(buenos_aires) == "34°36.7'S 058°25.3'W"
    assert str(buenos_aires.latitude) == "34°36.7'S"
    assert str(buenos_aires.longitude) == "058°25.3'W"


def test_parse_buenos_aires():
    buenos_aires = Position.parse("34°36.7'S 058°25.3'W")

    assert str(buenos_aires.latitude) == "34°36.7'S"
    assert str(buenos_aires.longitude) == "058°25.3'W"
    assert str(buenos_aires) == "34°36.7'S 058°25.3'W"
