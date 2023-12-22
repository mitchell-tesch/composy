"""
Composy - Compos API python wrapper
Compos file definition - Slab Concrete Material
"""
__all__ = ['SlabConcreteMaterial']

from enum import StrEnum

# Concrete Grade enumerations
class ConcGrade(StrEnum):
    C20 = 'C20'
    C25 = 'C25'
    C30 = 'C30'
    C32 = 'C32'
    C40 = 'C40'
    C50 = 'C50'
    C60 = 'C60'
    C65 = 'C65'
    C70 = 'C70'
    C80 = 'C80'
    C90 = 'C90'
    C100 = 'C100'
    C20_25 = 'C20/25'
    C25_30 = 'C25/30'
    C30_37 = 'C30/37'
    C35_45 = 'C35/45'
    C40_50 = 'C40/50'
    C45_55 = 'C45/55'
    C50_60 = 'C50/60'
    C55_67 = 'C55/67'
    C60_75 = 'C60/75'
    LC20_22 = 'LC20/22'
    LC25_28 = 'LC25/28'
    LC30_33 = 'LC30/33'
    LC35_38 = 'LC35/38'
    LC40_44 = 'LC40/44'
    LC45_50 = 'LC45/50'
    LC50_55 = 'LC50/55'
    LC55_60 = 'LC55/60'
    LC60_66 = 'LC60/66'

# Concrete Type enumerations
class ConcType(StrEnum):
    LIGHT = 'LIGHT'
    NORMAL = 'NORMAL'

# Concrete Density Class enumerations
class DensityClass(StrEnum):
    D801 = 'D801_1000'
    D1001 = 'D1001_1200'
    D1201 = 'D1201_1400'
    D1401 = 'D1401_1600'
    D1601 = 'D1601_1800'
    D1801 = 'D1801_2000'
    NOT_APPLY = 'NOT_APPLY'


class SlabConcreteMaterial():
    _density_user_defined = {True: 'USER_DENSITY',
                             False: 'CODE_DENSITY'}
    
    _e_ratio_user_defined = {True: 'USER_E_RATIO',
                             False: 'CODE_E_RATIO'}
    
    _shrink_user_defined = {True: 'USER_E_RATIO',
                            False: 'CODE_E_RATIO'}
    
    def __init__(self,
                 member_name,
                 grade: ConcGrade,
                 type: ConcType = ConcType.NORMAL,
                 is_density_user_defined: bool = False,
                 density: float = 2400.0,
                 density_class: DensityClass = DensityClass.NOT_APPLY,
                 percent_live_long: float = 0.33,
                 is_e_ratio_user_defined: bool = False,
                 e_ratio_short: float = 0.0,
                 e_ratio_long: float = 0.0,
                 e_ratio_vib: float = 0.0,
                 e_ratio_shrink: float = 0.0,
                 is_shrink_user_defined: bool = False,
                 shrink_strain: float = 0.0):
        self.member_name = member_name
        self.grade = grade
        self.type = type
        self.is_density_user_defined = is_density_user_defined
        self.density_type = self._density_user_defined[is_density_user_defined]
        self.density = density
        self.density_class = density_class
        if is_density_user_defined:
            self.density_class = ''
        self.percent = percent_live_long
        self.is_e_ratio_user_defined = is_e_ratio_user_defined
        self.e_ratio_type = self._e_ratio_user_defined[is_e_ratio_user_defined]
        if is_e_ratio_user_defined:
            self.e_ratio_short = e_ratio_short
            self.e_ratio_long = e_ratio_long
            self.e_ratio_vibe = e_ratio_vib
            self.e_ratio_shrink = e_ratio_shrink
        else:
            self.e_ratio_short = ''
            self.e_ratio_long = ''
            self.e_ratio_vibe = ''
            self.e_ratio_shrink = ''
        self.is_shrink_user_defined = is_shrink_user_defined
        self.shrink_type = self._shrink_user_defined[is_shrink_user_defined]
        if is_shrink_user_defined:
            self.shrink_strain = shrink_strain
        else:
            self.shrink_strain = ''
  
    def _definition_list(self):
        definitions = [self.grade, self.type, self.density_type]
        if self.is_density_user_defined:
            definitions.append(self.density)
        else:
            definitions.append(self.density_class)
        definitions.extend([self.percent, self.e_ratio_type])
        if self.is_e_ratio_user_defined:
            definitions.extend([self.e_ratio_short, self.e_ratio_long, self.e_ratio_vibe, self.e_ratio_shrink])
        definitions.append(self.shrink_type)
        if self.is_shrink_user_defined:
            definitions.append(self.shrink_strain)
        return definitions

    def __repr__(self) -> str:
        return f"SLAB_CONCRETE_MATERIAL({','.join(self._definition_list())})"

    def __str__(self) -> str:
        return f"SLAB_CONCRETE_MATERIAL,{self.member_name},{','.join(self._definition_list())}"
