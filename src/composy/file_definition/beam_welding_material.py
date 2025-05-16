"""
Composy - Compos API python wrapper
Compos file definition - Beam Welding Material
"""

__all__ = ['BeamWeldingMaterial']

from enum import StrEnum


# Standard Welding Material Grades enumerations
class StdSWeldingGrade(StrEnum):
    GRADE_35 = 'Grade 35'
    GRADE_42 = 'Grade 42'
    GRADE_50 = 'Grade 50'


class BeamWeldingMaterial:
    def __init__(self, member_name, material_grade: StdSWeldingGrade):
        self.member_name = member_name
        self.material_grade = material_grade

    def __repr__(self) -> str:
        return f'BEAM_WELDING_MATERIAL({self.material_grade})'

    def __str__(self) -> str:
        return f'BEAM_WELDING_MATERIAL,{self.member_name},{self.material_grade}'
