"""
Composy - Compos API python wrapper
Compos file definition - Decking User
"""

__all__ = ['DeckingUser']

from enum import StrEnum


# Decking type enumerations
class DeckingType(StrEnum):
    USER = 'USER_DEFINED'
    NONE = 'NO_DECKING '


class DeckingUser:
    _jointed = {True: 'DECKING_JOINTED', False: 'DECKING_CONTINUED'}
    _welded = {True: 'JOINT_WELDED', False: 'JOINT_NOT_WELD'}

    def __init__(
        self,
        member_name,
        type: DeckingType,
        b1: float,
        b2: float,
        b3: float,
        b4: float,
        b5: float,
        d: float,
        t: float,
        fy: float,
        angle: float,
        is_jointed: bool = False,
        is_welded: bool = False,
    ):
        self.member_name = member_name
        self.type = type
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
        self.b4 = b4
        self.b5 = b5
        self.d = d
        self.t = t
        self.fy = fy
        self.angle = angle
        self.is_jointed = self._jointed[is_jointed]
        self.is_welded = self._welded[is_welded]

    def __repr__(self) -> str:
        return f'DECKING_USER({self.type},{self.b1},{self.b2},{self.b3},{self.d},{self.t},{self.b4},{self.b5},\
            {self.fy},{self.angle},{self.is_jointed},{self.is_welded})'

    def __str__(self) -> str:
        return f'DECKING_USER,{self.member_name},{self.type},{self.b1},{self.b2},{self.b3},{self.d},{self.t},\
            {self.b4},{self.b5},{self.fy},{self.angle},{self.is_jointed},{self.is_welded}'
