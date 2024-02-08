"""
Contain all class to handle converting
"""


class UnitConverter:

    @staticmethod
    def convert(val: float, from_u: 'Enum', to_u: 'Enum'):
        return (((val - from_u.value[1]) * from_u.value[0]) / to_u.value[0]) + to_u.value[1]






