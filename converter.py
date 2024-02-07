"""
Contain all class to handle converting
"""

class UnitConverter:

    @staticmethod
    def convert(val, from_u, to_u):
        return (((val - from_u.value[1]) * from_u.value[0]) / to_u.value[0]) + to_u.value[1]






