"""
Composy - Compos API python wrapper
Compos file definition - Stud Definition
"""

__all__ = ['StudDefinition']

from enum import StrEnum


# Stud Type and Name enumerations
class StudType(StrEnum):
    STANDARD = 'STANDARD'
    USER_DEFINED = 'USER_DEFINED'
    NON_COMPOSITE = 'NON_COMPOSITE'


class StudName(StrEnum):
    D13_L65 = '13mm/65mm'
    D16_L75 = '16mm/75mm'
    D19_L75 = '19mm/75mm'
    D19_L100 = '19mm/100mm'
    D19_L125 = '19mm/125mm'
    D22_L100 = '22mm/100mm'
    D25_L100 = '25mm/100mm'


class StudDefinition:
    _is_reduced = {True: 'REDUCED_YES', False: 'REDUCED_NO'}

    _is_deck_welded = {True: 'WELDED_YES', False: 'WELDED_NO'}

    def __init__(
        self,
        member_name,
        stud_type: StudType,
        stud_name: StudName,
        stud_dia: float,
        stud_height: float,
        stud_fy: float,
        is_reduced: bool,
        is_deck_welded: bool = True,
    ):
        self.member_name = member_name
        self.stud_type = stud_type
        if stud_type == StudType.STANDARD:
            self.name = stud_name
            self.deck_welded = self._is_deck_welded[is_deck_welded]
        elif stud_type == StudType.USER_DEFINED:
            self.name = ''
            self.dia = stud_dia
            self.height = stud_height
            self.fy = stud_fy
            self.reduced = self._is_reduced[is_reduced]
            self.deck_welded = self._is_deck_welded[is_deck_welded]
        else:
            self.name = ''
            self.dia = ''
            self.height = ''
            self.fy = ''
            self.reduced = ''
            self.deck_welded = ''

    def __repr__(self) -> str:
        match self.stud_type:
            case StudType.STANDARD:
                return f'STUD_DEFINITION({self.stud_type},{self.name},{self.deck_welded})'
            case StudType.USER_DEFINED:
                return f'STUD_DEFINITION({self.stud_type},{self.dia},{self.height},{self.fy},{self.reduced},{self.deck_welded})'
        return f'STUD_DEFINITION({self.stud_type})'

    def __str__(self) -> str:
        match self.stud_type:
            case StudType.STANDARD:
                return f'STUD_DEFINITION,{self.member_name},{self.stud_type},{self.name},{self.deck_welded})'
            case StudType.USER_DEFINED:
                return f'STUD_DEFINITION,{self.member_name},{self.stud_type},{self.dia},{self.height},{self.fy},{self.reduced},{self.deck_welded})'
        return f'STUD_DEFINITION,{self.member_name},{self.stud_type})'
