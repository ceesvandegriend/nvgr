from dataclasses import dataclass

from nvgr import Latitude, Longitude


@dataclass
class Location:
    def __init__(self, latitude: Latitude, longitude: Longitude):
        self.latitude = latitude
        self.longitude = longitude

    def __repr__(self):
        lat = str(self.latitude)
        lng = str(self.longitude)
        return f"{lat} {lng}"
