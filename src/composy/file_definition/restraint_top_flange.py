"""
Composy - Compos API python wrapper
Compos file definition - Restraint Top Flange
"""

__all__ = ['RestraintTopFlange']


class RestraintTopFlange:
    _is_top_flange_fixed = {True: 'TOP_FLANGE_FIXED', False: 'TOP_FLANGE_FREE'}

    def __init__(
        self,
        member_name,
        is_fixed: bool,
    ):
        self.member_name = member_name
        self.restraint = self._is_top_flange_fixed[is_fixed]

    def __repr__(self) -> str:
        return f'RESTRAINT_TOP_FALNGE({self.restraint})'

    def __str__(self) -> str:
        return f'RESTRAINT_TOP_FALNGE,{self.member_name},{self.restraint}'
