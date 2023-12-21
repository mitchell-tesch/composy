"""
Composy - Compos API python wrapper
Compos file definition - Slab Concrete Material
"""
__all__ = ['SlabConcreteMaterial']

from enum import StrEnum

# Concrete Grade enumerations
class DefGrade(StrEnum):
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

# Concrete Type enumerations
class DefType(StrEnum):
    LIGHT = 'LIGHT'
    NORMAL = 'NORMAL'
    
# Concrete Density Type enumerations
class DefDensityType(StrEnum):
    CODE_DENSITY = 'CODE_DENSITY'
    USER_DENSITY = 'USER_DENSITY'

# Concrete Density Class enumerations
class DefDensityClass(StrEnum):
    NOT_APPLY = 'NOT_APPLY'
    
# Concrete Elastic Modulus Class enumerations
# class DefERatioType(StrEnum):
#     # _E_user_defined = {True: 'USER_E_RATIO',
#     #                  False: 'CODE_E_RATIO'}
#     CODE_E_RATIO = 'CODE_E_RATIO'
#     USER_E_RATIO = 'USER_E_RATIO'
    

# # Concrete Shrinkage Strain Class enumerations
# class DefShrinkType(StrEnum):
#     CODE_STRAIN = 'CODE_STRAIN'
#     USER_STRAIN = 'USER_STRAIN'


class SlabConcreteMaterial():
    _e_user_defined = {True: 'USER_E_RATIO',
                     False: 'CODE_E_RATIO'}
    
    _strain_user_defined = {True: 'USER_E_RATIO',
                     False: 'CODE_E_RATIO'}
    
    def __init__(self,
                 member_name,
                 is_e_user_defined: bool = False,
                 is_strain_user_defined: bool = False,
                 grade: DefGrade, #
                 type: DefType, #
                 density_type: DefDensityType, #
                 density: float, #
                 density_class: DefDensityClass, #
                 percent: float = 0.33,
                 e_ratio_type: float = 0.0,
                 e_ratio_short: float = 0.0,
                 e_ratio_long: float = 0.0,
                 e_ratio_vib: float = 0.0,
                 e_ratio_shrink: float = 0.0,
                 shrink_type: float = 0.0,
                 shrink_strain: float = 0.0,
                 ):
        self.member_name = member_name
        self.grade = grade
        self.type = type
        self.density_type = density_type
        self.density = density
        self.density_class = density_class
        self.percent = percent
        if is_e_user_defined:
            self.e_ratio_type = e_ratio_type
            self.e_ratio_short = e_ratio_short
            self.e_ratio_long = e_ratio_long
            self.e_ratio_vibe = e_ratio_vib
            self.e_ratio_shrink = e_ratio_shrink
        else:
            self.e_ratio_type = ''
            self.e_ratio_short = ''
            self.e_ratio_long = ''
            self.e_ratio_vibe = ''
            self.e_ratio_shrink = ''
        if is_strain_user_defined:
            self.shrink_type = shrink_type
            self.shrink_strain = shrink_strain
        else:
            self.shrink_type = ''
            self.shrink_strain = ''
            
        
        
    def __repr__(self) -> str:
        return f"FINAL_RESTRAINT_POINT({self.grade},{self.type},{self.density_type},{self.density},{self.density_class},{self.percent},{self.e_ratio_type})"

    def __str__(self) -> str:
        return f"FINAL_RESTRAINT_POINT,{self.member_name},{self.grade},{self.type},{self.density_type},{self.density},{self.e_ratio_type}"