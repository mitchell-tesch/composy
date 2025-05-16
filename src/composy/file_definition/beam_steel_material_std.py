"""
Composy - Compos API python wrapper
Compos file definition - Beam Steel Material Std
"""

__all__ = ['BeamSteelMaterialStd']

from enum import StrEnum


# Standard Steel Material Grades enumerations
class StdSteelGrade(StrEnum):
    S275 = 'S275'
    S355 = 'S355'
    S460 = 'S460'
    S235_EN = 'S235_EN'
    S275_EN = 'S275_EN'
    S355_EN = 'S355_EN'
    S460_EN = 'S460_EN'
    AS_300 = '300(AS3678)'
    AS_350 = '350(AS3678)'
    AS_400 = '400(AS3678)'


class BeamSteelMaterialStd:
    def __init__(self, member_name, material_grade: StdSteelGrade):
        self.member_name = member_name
        self.material_grade = material_grade

    def __repr__(self) -> str:
        return f'BEAM_STEEL_MATERIAL_STD({self.material_grade})'

    def __str__(self) -> str:
        return f'BEAM_STEEL_MATERIAL_STD,{self.member_name},{self.material_grade}'
