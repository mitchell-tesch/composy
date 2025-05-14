"""
Composy - Compos API python wrapper
Compos file definition - EC4 Load Comb Factors
"""

__all__ = ['EcDesignOption']

from enum import StrEnum


# Load combination enumerations
class EcAnnex(StrEnum):
    EC = 'EC4_GENERIC'
    EC_UK = 'EC4_UK'


class EcCementClass(StrEnum):
    CLASS_S = 'EC4_CLASS_S'
    CLASS_N = 'EC4_CLASS_N'
    CLASS_R = 'EC4_CLASS_R'


class EcDesignOption:
    _include_shrink_defl = {True: 'SHRINKAGE_DEFORM_EC4_YES', False: 'SHRINKAGE_DEFORM_EC4_NO'}

    _ratio_ignore_shrink_defl = {True: 'IGNORE_SHRINKAGE_DEFORM_YES', False: 'IGNORE_SHRINKAGE_DEFORM_NO'}

    _approx_modular_ratio = {True: 'APPROXIMATE_E_RATIO_YES', False: 'APPROXIMATE_E_RATIO_NO'}

    def __init__(
        self,
        member_name,
        include_shrink_defl: bool,
        ratio_ignore_shrink_defl: bool,
        approx_modular_ratio: bool,
        ec_annex: EcAnnex,
        cement_class: EcCementClass,
        creep_factor_long: float = 1.1,
        creep_factor_shrink: float = 0.55,
        age_at_load_creep: int = 28,
        age_at_load_shrink: int = 1,
        age_long_creep: int = 36500,
        age_long_shrink: int = 36500,
        relative_humidity_long: int = 50,
        relative_humidity_shrink: int = 50,
    ):
        self.member_name = member_name
        self.include_shrink_defl = self._include_shrink_defl[include_shrink_defl]
        self.ratio_ignore_shrink_defl = self._ratio_ignore_shrink_defl[ratio_ignore_shrink_defl]
        self.approx_modular_ratio = self._approx_modular_ratio[approx_modular_ratio]
        self.ec_annex = ec_annex
        self.cement_class = cement_class
        self.creep_factor_long = creep_factor_long
        self.creep_factor_shrink = creep_factor_shrink
        self.age_at_load_creep = age_at_load_creep
        self.age_at_load_shrink = age_at_load_shrink
        self.age_long_creep = age_long_creep
        self.age_long_shrink = age_long_shrink
        self.relative_humidity_long = relative_humidity_long
        self.relative_humidity_shrink = relative_humidity_shrink

    def __repr__(self) -> str:
        return f'EC4_DESIGN_OPTION({self.include_shrink_defl},{self.ratio_ignore_shrink_defl},{self.approx_modular_ratio},{self.ec_annex},{self.cement_class},\
            {self.creep_factor_long},{self.creep_factor_shrink},{self.age_at_load_creep},{self.age_at_load_shrink},{self.age_long_creep},{self.age_long_shrink},\
                {self.relative_humidity_long},{self.relative_humidity_shrink})'

    def __str__(self) -> str:
        return f'EC4_DESIGN_OPTION,{self.member_name},{self.include_shrink_defl},{self.ratio_ignore_shrink_defl},{self.approx_modular_ratio},\
            {self.ec_annex},{self.cement_class},{self.creep_factor_long},{self.creep_factor_shrink},{self.age_at_load_creep},{self.age_at_load_shrink},\
                {self.age_long_creep},{self.age_long_shrink},{self.relative_humidity_long},{self.relative_humidity_shrink}'
