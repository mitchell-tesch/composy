"""
Composy - Compos API python wrapper
Compos file definition - Web Opening
"""
__all__ = ['WebOpening']

from enum import StrEnum

# Mesh and mesh direction enumerations
class OpeningShape(StrEnum):
    RECTANGULAR = 'RECTANGULAR'
    CIRCULAR = 'CIRCULAR'
    LEFT_NOTCH = 'LEFT_NOTCH'
    RIGHT_NOTCH = 'RIGHT_NOTCH'

class MeshDirection(StrEnum):
    PARALLEL = 'PARALLEL'
    PERPENDICULAR = 'PERPENDICULAR'


class WebOpening():
    _is_stiffened = {True: 'STIFFENER_YES',
                     False: 'STIFFENER_NO'}
    
    _stiff_both_sides = {True: 'BOTH_SIDE_STIFFENER',
                             False: 'ONE_SIDE_STIFFENER'}

    def __init__(self,
                 member_name,
                 shape: OpeningShape,
                 width: float,
                 height: float,
                 pos_from_left: float,
                 pos_from_top: float,
                 is_stiffened: bool,
                 is_stiff_both_sides: bool,
                 stiff_offset: float,
                 top_stiff_width: float,
                 top_stiff_thick: float,
                 bot_stiff_width: float,
                 bot_stiff_thick: float):
        self.member_name = member_name
        self.shape = shape
        self.width = width
        self.height = height
        self.pos_from_left = pos_from_left
        self.pos_from_top = pos_from_top
        self.stiffened = self._is_stiffened[is_stiffened]
        self.stiff_both_sides = self._stiff_both_sides[is_stiff_both_sides]
        self.stiff_offset = stiff_offset
        self.top_stiff_width = top_stiff_width
        self.top_stiff_thick = top_stiff_thick
        self.bot_stiff_width = bot_stiff_width
        self.bot_stiff_thick = bot_stiff_thick

    def __repr__(self) -> str:
        return f"WEB_OPEN_DIMENSION({self.shape},{self.width},{self.height},{self.pos_from_left},{self.pos_from_top},\
            {self.stiffened},{self.stiff_both_sides},{self.stiff_offset},{self.top_stiff_width},{self.top_stiff_thick},\
                {self.bot_stiff_width},{self.bot_stiff_thick})"

    def __str__(self) -> str:
        return f"WEB_OPEN_DIMENSION,{self.member_name},{self.shape},{self.width},{self.height},{self.pos_from_left},\
            {self.pos_from_top}, {self.stiffened},{self.stiff_both_sides},{self.stiff_offset},\
                {self.top_stiff_width},{self.top_stiff_thick}{self.bot_stiff_width},{self.bot_stiff_thick}"