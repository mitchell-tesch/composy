"""
Composy - Compos API python wrapper
Compos file definition - Stud Grade
"""
__all__ = ['StudGrade']

from enum import StrEnum

# Standard sStud Grade enumerations
class StandardStudGrade(StrEnum):
    SD1_EN13918 = 'SD1_EN13918'
    SD2_EN13918 = 'SD2_EN13918'
    SD3_EN13918 = 'SD3_EN13918'


class StudGrade():
    _is_code_grade = {True: 'CODE_GRADE_YES',
                      False: 'CODE_GRADE_NO '}

    def __init__(self,
                 member_name,
                 is_code_grade: bool,
                 stud_grade: StandardStudGrade,
                 stud_fu: float):
        self.member_name = member_name
        self.is_code_grade = self._is_code_grade[is_code_grade]
        if is_code_grade:
            self.grade = stud_grade
        else:
            self.grade = stud_fu

    def __repr__(self) -> str:
        return f"STUD_GRADE({self.is_code_grade},{self.grade})"

    def __str__(self) -> str:
        return f"STUD_GRADE,{self.member_name},{self.is_code_grade},{self.grade}"
