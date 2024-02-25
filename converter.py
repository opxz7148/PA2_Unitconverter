"""
Contain all class to handle converting
"""
from unittype import UnitType


class UnitConverter:

    @staticmethod
    def convert(unittype: UnitType, val: float, from_unit: str, to_unit: str):

        unit = unittype.value[1]

        from_u_factor = unit[from_unit]

        to_u_factor = unit[to_unit]

        return (((val - from_u_factor.value[1]) * from_u_factor.value[0]) / to_u_factor.value[0]) + to_u_factor.value[1]

    @staticmethod
    def get_unit_type(only=None):
        if not only:
            return [unit for unit in UnitType]
        else:
            return UnitType[only]

    @staticmethod
    def get_units(unittype: UnitType):
        return [unit.name.replace("_", " ") for unit in unittype.value[1]]
