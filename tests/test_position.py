from nvgr import Latitude, Longitude, Position


def test_rotterdam():
    # Google Maps: Rotterdam Stadhuis: 51.922743, 4.479305
    # 51°55.4'N 004°28.8'E
    lat = Latitude(51.922743)
    lng = Longitude(4.479305)
    rdam = Position(lat, lng)

    assert str(rdam.latitude) == "51°55.4'N"
    assert str(rdam.longitude) == "004°28.8'E"
    assert str(rdam) == "51°55.4'N 004°28.8'E"
