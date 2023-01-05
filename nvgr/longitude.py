from dataclasses import dataclass


@dataclass
class Longitude:
    def __init__(self):
        self.degrees = 0.0

    def __repr__(self):
        return f"{self.degrees:07.3f}\u00b0"
