"""
Composy - Compos API python wrapper
Compos file definition - Slab Dimension
"""
__all__ = ['SlabDimension']

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


class SlabDimension():
    _is_tapered = {True: 'TAPERED_YES',
                   False: 'TAPERED_NO'}
    _override_eff_width = {True: 'EFFECTIVE_WIDTH_YES',
                           False: 'EFFECTIVE_WIDTH_NO'}

    def __init__(self,
                 member_name,
                 num_slab: int,
                 slab_index: int,
                 depth: float,
                 width_left: float,
                 width_right: float,
                 eff_width_left: float,
                 eff_width_right: float,
                 is_tapered: bool = False,
                 override_eff_width: bool = False):
        self.member_name = member_name
        self.num_slab = num_slab
        self.slab_index = slab_index
        self.depth = depth
        self.width_left = width_left
        self.width_right = width_right
        self.is_tapered = self._is_tapered[is_tapered]
        self.override = override_eff_width
        self.override_eff_width = self._override_eff_width[override_eff_width]
        if override_eff_width:
            self.eff_width_left = eff_width_left
            self.eff_width_right = eff_width_right
        else:
            self.eff_width_left = ''
            self.eff_width_right = ''

    def __repr__(self) -> str:
        if self.override:
            return f"SLAB_DIMENSION({self.num_slab},{self.slab_index},{self.depth},{self.width_left},{self.width_right},\
                {self.is_tapered},{self.override_eff_width},{self.eff_width_left},{self.eff_width_right})"
        return f"SLAB_DIMENSION({self.num_slab},{self.slab_index},{self.depth},{self.width_left},{self.width_right},\
            {self.is_tapered},{self.override_eff_width})"

    def __str__(self) -> str:
        if self.override:
            return f"SLAB_DIMENSION,{self.member_name},{self.num_slab},{self.slab_index},{self.depth},{self.width_left},\
                {self.width_right},{self.is_tapered},{self.override_eff_width},{self.eff_width_left},{self.eff_width_right}"
        return f"SLAB_DIMENSION,{self.member_name},{self.num_slab},{self.slab_index},{self.depth},{self.width_left},\
                {self.width_right},{self.is_tapered},{self.override_eff_width}"
