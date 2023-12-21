"""
Composy - Compos API python wrapper
Compos file definition - Stud NCCI Limit Apply
"""
__all__ = ['StudNcciApply']

class StudNcciApply():
    _apply_ncci_limits = {True: 'YES',
                          False: 'NO'}

    def __init__(self,
                 member_name,
                 apply_ncci_limits: bool):
        self.member_name = member_name
        self.apply = self._apply_ncci_limits[apply_ncci_limits]

    def __repr__(self) -> str:
        return f"STUD_NCCI_LIMIT_APPLY({self.apply})"

    def __str__(self) -> str:
        return f"STUD_NCCI_LIMIT_APPLY,{self.member_name},{self.apply}"
