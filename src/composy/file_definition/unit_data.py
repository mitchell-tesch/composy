"""
Composy - Compos API python wrapper
Compos file definition - Unit Data
"""

__all__ = ['UnitData']

from enum import StrEnum

# unit scaling factor to SI units
SI_UNIT_FACTOR = {
    'N': 1.0,
    'kN': 1.0e-3,
    'MN': 1.0e-6,
    'mm': 1.0e3,
    'cm': 1.0e2,
    'm': 1.0,
    'Pa': 1.0,
    'kPa': 1.0e-3,
    'MPa': 1.0e-6,
    'GPa': 1.0e-9,
    'kg': 1.0,
    't': 1.0e-3,
}


# Unit data enumerations
class ForceUnit(StrEnum):
    N = 'N'
    kN = 'kN'
    MN = 'MN'


class LengthUnit(StrEnum):
    mm = 'mm'
    cm = 'cm'
    m = 'm'


class StressUnit(StrEnum):
    Pa = 'Pa'
    kPa = 'kPa'
    MPa = 'MPa'
    GPa = 'GPa'


class MassUnit(StrEnum):
    kg = 'kg'
    t = 't'


# Unit data object - generic per unit type
class Unit:
    def __init__(self, unit_type: str, unit_name: str):
        self.option = unit_type.upper()
        self.name = unit_name
        self.factor = SI_UNIT_FACTOR[unit_name]

    def __repr__(self) -> str:
        return f'{self.option}_{self.name}'

    def __str__(self) -> str:
        return f'UNIT_DATA,{self.option},{self.name},{self.factor}'


# Compos file units object - collection of all unit types
class UnitData:
    ForceUnit = ForceUnit
    LengthUnit = LengthUnit
    StressUnit = StressUnit
    MassUnit = MassUnit

    def __init__(
        self,
        force_unit: ForceUnit = ForceUnit.N,
        length_unit: LengthUnit = LengthUnit.m,
        disp_unit: LengthUnit = LengthUnit.m,
        section_unit: LengthUnit = LengthUnit.m,
        stress_unit: StressUnit = StressUnit.Pa,
        mass_unit: MassUnit = MassUnit.kg,
    ):
        self.force = Unit('force', force_unit)
        self.length = Unit('length', length_unit)
        self.disp = Unit('disp', disp_unit)
        self.section = Unit('section', section_unit)
        self.stress = Unit('stress', stress_unit)
        self.mass = Unit('mass', mass_unit)

    def __repr__(self) -> str:
        unit_reprs = [unit.__repr__() for unit in self.__dict__.values()]
        return f'UNIT_DATA({",".join(unit_reprs)})'

    def get_unit_strings(self) -> list[str]:
        unit_strings = [str(unit) for unit in self.__dict__.values()]
        return unit_strings
