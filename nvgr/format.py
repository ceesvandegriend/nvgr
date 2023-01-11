import math
import re


class NauticalFormatter:
    @classmethod
    def formatLatitude(cls, degrees: float) -> str:
        s = "N" if degrees >= 0.0 else "S"
        d = math.floor(abs(degrees))
        m = (abs(degrees) - d) * 60.0

        return f"{d:02.0f}\u00b0{m:04.1f}'{s}"

    @classmethod
    def parseLatitude(cls, fmt: str) -> float:
        match = re.search("([0123456789]{2})(.+)([0123456789.]{4})(.*)([NnSs])", fmt)

        if match:
            d = float(match.group(1))
            m = float(match.group(3))
            s = match.group(5)
        else:
            raise ValueError(fmt)

        if s in ["S", "s"]:
            degrees = (d + m / 60) * -1
        else:
            degrees = d + m / 60
        return degrees

    @classmethod
    def formatLongitude(cls, degrees: float) -> str:
        s = "E" if degrees >= 0.0 else "W"
        d = math.floor(abs(degrees))
        m = (abs(degrees) - d) * 60.0

        return f"{d:03.0f}\u00b0{m:04.1f}'{s}"

    @classmethod
    def parseLongitude(cls, fmt: str) -> float:
        match = re.search("([0123456789]{3})(.+)([0123456789.]{4})(.*)([EeWw])", fmt)

        if match:
            d = float(match.group(1))
            m = float(match.group(3))
            s = match.group(5)
        else:
            raise ValueError(fmt)

        if s in ["W", "w"]:
            degrees = (d + m / 60) * -1
        else:
            degrees = d + m / 60
        return degrees

    @classmethod
    def formatCourse(cls, degrees: float) -> str:
        return f"{degrees:05.1f}\u00b0"

    @classmethod
    def formatDistance(cls, degrees: float) -> str:
        distance = degrees * 60
        return f"{distance:0.1f}'"

    @classmethod
    def formatPosition(cls, latitude: float, longitude: float) -> str:
        lat = cls.formatLatitude(latitude)
        lng = cls.formatLongitude(longitude)
        return f"{lat} {lng}"

    @classmethod
    def parsePosition(cls, fmt: str):
        match = re.search(
            "([0123456789]{2})(.+)([0123456789.]{4})(.*)([NnSs])(.+)([0123456789]{3})(.+)([0123456789.]{4})(.*)([EeWw])",
            fmt,
        )

        if match:
            d0 = float(match.group(1))
            m0 = float(match.group(3))
            s0 = match.group(5)
            d1 = float(match.group(7))
            m1 = float(match.group(9))
            s1 = match.group(11)
        else:
            raise ValueError(fmt)

        if s0 in ["S", "s"]:
            lat = (d0 + m0 / 60) * -1
        else:
            lat = d0 + m0 / 60

        if s1 in ["W", "w"]:
            lng = (d1 + m1 / 60) * -1
        else:
            lng = d1 + m1 / 60

        return lat, lng


# set default Formatter to NauticalFormatter
formatter = NauticalFormatter()
