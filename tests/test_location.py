from nvgr import Latitude, Longitude, Location


def test_rotterdam():
    # Google Maps: Rotterdam Stadhuis: 51.922743, 4.479305
    # 51°55.4'N 004°28.8'E
    lat = Latitude(51.922743)
    lng = Longitude(4.479305)
    rotterdam = Location(lat, lng)

    assert str(rotterdam.latitude) == "51°55.4'N"
    assert str(rotterdam.longitude) == "004°28.8'E"
    assert str(rotterdam) == "51°55.4'N 004°28.8'E"
