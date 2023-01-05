from dataclasses import dataclass


@dataclass
class Latitude:
    def __init__(self):
        self.degrees = 0.0

    def __repr__(self):
        return f"{self.degrees:06.3f}\u00b0"
