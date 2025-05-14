"""
Composy - Compos API python wrapper
Compos file definition - Rebar Material
"""

__all__ = ['RebarMaterial']

from enum import StrEnum


# Reinforcing Grade enumerations
class ReinforcementGrade(StrEnum):
    BS_250R = '250R'
    BS_460T = '460T'
    BS_500X = '500X'
    BS_1770 = '1770'
    EC_500A = '500A'
    EC_500B = '500B'
    EC_500C = '500C'


class RebarMaterial:
    _user_defined = {True: 'USER_DEFINED', False: 'STANDARD'}

    def __init__(
        self,
        member_name,
        is_user_defined: bool = False,
        grade: ReinforcementGrade = ReinforcementGrade.EC_500A,
        fy: float = 500,
    ):
        self.member_name = member_name
        self.is_user_defined = is_user_defined
        self.type = self._user_defined[is_user_defined]
        if is_user_defined:
            self.grade = fy
        else:
            self.grade = grade

    def __repr__(self) -> str:
        return f'REBAR_MATERIAL({self.type},{self.grade})'

    def __str__(self) -> str:
        return f'REBAR_MATERIAL,{self.member_name},{self.type},{self.grade}'
