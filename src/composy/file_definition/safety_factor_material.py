"""
Composy - Compos API python wrapper
Compos file definition - Safety Factor Material
"""

__all__ = ['SafetyFactorMaterial']


class SafetyFactorMaterial:
    def __init__(
        self,
        member_name,
        steel_yield: float,
        steel_buckling: float,
        steel_ultimate: float,
        conc_comp: float,
        conc_shear: float,
        decking: float,
        stud: float,
        reinforcement: float,
    ):
        self.member_name = member_name
        self.steel_yield = steel_yield
        self.steel_buckling = steel_buckling
        self.steel_ultimate = steel_ultimate
        self.conc_comp = conc_comp
        self.conc_shear = conc_shear
        self.decking = decking
        self.stud = stud
        self.reinforcement = reinforcement

    def __repr__(self) -> str:
        return f'SAFETY_FACTOR_MATERIAL({self.steel_yield},{self.steel_buckling},{self.steel_ultimate},\
            {self.conc_comp},{self.conc_shear},{self.decking},{self.stud},{self.reinforcement})'

    def __str__(self) -> str:
        return f'SAFETY_FACTOR_MATERIAL,{self.member_name},{self.steel_yield},{self.steel_buckling},\
            {self.steel_ultimate},{self.conc_comp},{self.conc_shear},{self.decking},{self.stud},\
                {self.reinforcement}'
