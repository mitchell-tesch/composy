"""
Composy - Compos API python wrapper
Compos file definition - Design Option
"""
__all__ = ['DesignOption']

from enum import StrEnum

# Design code and Construction type enumerations
class DesignCode(StrEnum):
    BS5950_2010 = 'BS5950-3.1:1990+A1:2010'
    EN1994_1_1_2004 = 'EN1994-1-1:2004'
    HKSUOS_2011 = 'HKSUOS:2011'
    ASNZS2327_2017 = 'AS/NZS2327:2017'

class ConstructionType(StrEnum):
    PROPPED = 'PROPPED'
    UNPROPPED = 'UNPROPPED'


class DesignOption():    
    _beam_weight = {True: 'BEAM_WEIGHT_YES',
                    False: 'BEAM_WEIGHT_NO'}
    _slab_weight = {True: 'SLAB_WEIGHT_YES',
                    False: 'SLAB_WEIGHT_NO'}
    _shear_deform = {True: 'SHEAR_DEFORM_YES',
                     False: 'SHEAR_DEFORM_NO'}
    _thin_section = {True: 'THIN_SECTION_YES',
                     False: 'THIN_SECTION_NO'}

    def __init__(self,
                 member_name,
                 design_code: DesignCode,
                 construction_type: ConstructionType,
                 include_beam_weight: bool = True,
                 include_slab_weight: bool = True,
                 include_shear_deform: bool = True,
                 include_thin_flange: bool = False):
        self.member_name = member_name
        self.design_code = design_code
        self.construct_type = construction_type
        self.beam_weight = self._beam_weight[include_beam_weight]
        self.slab_weight = self._slab_weight[include_slab_weight]
        self.shear_deform = self._shear_deform[include_shear_deform]
        self.thin_section = self._thin_section[include_thin_flange]

    def __repr__(self) -> str:
        return f"DESIGN_OPTION({self.design_code},{self.beam_weight},{self.beam_weight},\
            {self.slab_weight},{self.shear_deform},{self.thin_section})"

    def __str__(self) -> str:
        return f"DESIGN_OPTION,{self.member_name},{self.design_code},{self.beam_weight},\
            {self.beam_weight},{self.slab_weight},{self.shear_deform},{self.thin_section}"
