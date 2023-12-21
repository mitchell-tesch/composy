"""
Composy - Compos API python wrapper
Compos file definition - Rebar Longitudinal
"""
__all__ = ['RebarLongitudinal']

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


class RebarLongitudinal():
    _user_defined = {True: 'USER_DEFINED',
                     False: 'PROGRAM_DESIGNED'}

    def __init__(self,
                 member_name,
                 is_user_defined: bool = False,
                 start: float = 0.0,
                 end:  float = 0.0,
                 diameter: int = 0,
                 spacing: float = 0.0,
                 cover: float = 0.0,
                 grade: ReinforcementGrade = ReinforcementGrade.EC_500A):
        self.member_name = member_name
        self.is_user_defined = is_user_defined
        self.type = self._user_defined[is_user_defined]
        if is_user_defined:
            self.start = start
            self.end = end
            self.diameter = diameter
            self.spacing = spacing
            self.cover = cover
            self.grade = grade
        else:
            self.start = ''
            self.end = ''
            self.diameter = ''
            self.spacing = ''
            self.cover = ''
            self.grade = ''

    def __repr__(self) -> str:
        if self.is_user_defined:
            return f"RREBAR_LONGITUDINAL({self.type},{self.start},{self.end},{self.diameter},\
                {self.spacing},{self.cover},{self.grade})"
        return f"RREBAR_LONGITUDINAL({self.type})"

    def __str__(self) -> str:
        if self.is_user_defined:
            return f"RREBAR_LONGITUDINAL,{self.member_name},{self.type},{self.start},{self.end},{self.diameter},\
                {self.spacing},{self.cover},{self.grade}"
        return f"RREBAR_LONGITUDINAL,{self.member_name},{self.type}"
