"""
Composy - Compos API python wrapper
Compos file definition - EC4 Load Comb Factors
"""

__all__ = ['EcLoadCombFactors']

from enum import StrEnum


# Load combination enumerations
class EcLoadComb(StrEnum):
    EC0 = 'EC0_6_10'
    EC0_WORST = 'EC0_WORST_6_10A_10B'
    USER_DEFINED = 'USER_DEFINED'


class EcLoadCombFactors:
    def __init__(
        self,
        member_name,
        load_comb: EcLoadComb,
        xi_const: float = 1.0,
        xi_final: float = 1.0,
        psi_const: float = 1.0,
        psi_final: float = 1.0,
    ):
        self.member_name = member_name
        self.load_comb = load_comb
        self.xi_const = xi_const
        self.xi_final = xi_final
        self.psi_const = psi_const
        self.psi_final = psi_final

    def __repr__(self) -> str:
        if self.load_comb == EcLoadComb.USER_DEFINED:
            return (
                f'EC4_DESIGN_OPTION({self.load_comb},{self.xi_const},{self.xi_final},{self.psi_const},{self.psi_final})'
            )
        return f'EC4_DESIGN_OPTION({self.member_name},{self.load_comb})'

    def __str__(self) -> str:
        if self.load_comb == EcLoadComb.USER_DEFINED:
            return f'EC4_DESIGN_OPTION,{self.member_name},{self.load_comb},{self.xi_const},{self.xi_final},{self.psi_const},{self.psi_final}'
        return f'EC4_DESIGN_OPTION,{self.member_name},{self.load_comb}'
