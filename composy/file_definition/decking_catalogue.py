"""
Composy - Compos API python wrapper
Compos file definition - Decking Catalogue
"""
__all__ = ['DeckingCatalogue']

from enum import StrEnum

# Decking Catalogue and Grade enumerations
class DeckingManufacturer(StrEnum):
    RLD = 'RLD'
    KINGSPAN = 'Kingspan'
    SMD = 'SMD'
    TATA = 'TATA'
    CMF = 'Corus_PMF'

class DeckingGrade(StrEnum):
    S280 = 'S280'
    S350 = 'S350'


class DeckingCatalogue():
    _jointed = {True: 'DECKING_JOINTED',
                False: 'DECKING_CONTINUED'}
    _welded = {True: 'JOINT_WELDED',
               False: 'JOINT_NOT_WELD'}

    def __init__(self,
                 member_name,
                 catalogue: DeckingManufacturer,
                 decking_name: str,
                 grade: DeckingGrade,
                 angle: float,
                 is_jointed: bool = False,
                 is_welded: bool = False):
        self.member_name = member_name
        self.catalogue = catalogue
        self.decking_name = decking_name
        self.grade = grade
        self.angle = angle
        self.is_jointed = self._jointed[is_jointed]
        self.is_welded = self._welded[is_welded]

    def __repr__(self) -> str:
        return f"DECKING_CATALOGUE({self.catalogue},{self.decking_name},{self.grade},{self.angle},\
            {self.is_jointed},{self.is_welded})"

    def __str__(self) -> str:
        return f"DECKING_CATALOGUE,{self.member_name},{self.catalogue},{self.decking_name},{self.grade},\
            {self.angle},{self.is_jointed},{self.is_welded}"
