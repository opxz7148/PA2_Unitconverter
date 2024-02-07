"""
Contain all class to handle converting
"""
from dataclasses import dataclass
from enum import Enum
from abc import ABC, abstractmethod
from unittype import UnitType


class UnitConverter(ABC):
    """
    Abstract class for each unit converter.
    """

    @abstractmethod
    def get_units(self):
        pass

    @abstractmethod
    def convert(self, val, from_u, to_u):
        pass


class LengthUnits(Enum):
    """
    All available unit in meter.
    """
    meter = 1.0
    kilometer = 1000
    centimeter = 0.01
    millimeter = 0.001
    nanometer = 1e-9
    astronomical_unit = 1.496e+11
    light_year = 9.461e+15
    sok = 0.5
    wa = 2

class LengthConverter(UnitConverter):
    """
    Controller class to handle converting request and any other request relate to converting.
    """

    @classmethod
    def get_units(cls):
        return [unit.name for unit in LengthUnits]

    @classmethod
    def convert(cls, val: float,  from_u: str, to_u: str) -> float:
        """
        Convert
        :param val: Value that want to convert
        :param from_u: Initial unit.
        :param to_u: Converted unit.
        :return: Converted length in float.
        """

        return (val * LengthUnits[from_u].value) / LengthUnits[to_u].value


