"""An enumeration of known types of units."""
from enum import Enum


class LengthUnits(Enum):
    """
    convert factor to meter (multiplier, offset)
    """
    Meter = (1.0, 0)
    Kilometer = (1000, 0)
    Centimeter = (0.01, 0)
    Millimeter = (0.001, 0)
    Nanometer = (1e-9, 0)
    Astronomical_unit = (1.496e+11, 0)
    Light_year = (9.461e+15, 0)
    Sok = (0.5, 0)
    Wa = (2, 0)


class AreaUnits(Enum):
    """
    convert factor to square meter (multiplier, offset)
    """
    Square_meter = (1.0, 0)
    Square_millimeter = (1e-6, 0)
    Square_kilometer = (1e+6, 0)
    Square_mile = (2.59e+6, 0)
    Square_yard = (0.836127, 0)
    Square_foot = (0.092903, 0)
    square_inch = (0.00064516, 0)
    Hectare = (10000, 0)
    Acre = (4046.86, 0)


class TempUnits(Enum):
    """
    convert factor to celcius (multiplier, offset)
    """
    Celcius = (1.0, 0)
    Farenheit = (5/9, 32)
    Kelvin = (1, 273.15)


class UnitType(Enum):
    """Define the unittypes here.  The value is the printable type name."""
    LENGTH = ("Length", LengthUnits)
    AREA = ("Area", AreaUnits)    # you can change Area to some other unittype
    TEMPERATURE = ("Temperature", TempUnits)

    def __str__(self):
        """Return the unittype name suitable for printing."""
        return self.value[0]