"""
Composy - Compos API python wrapper
Compos file definition - Stud EC4 Apply
"""
__all__ = ['StudEcApply']

class StudEcApply():
    _apply_ec4_min_shear = {True: 'YES',
                            False: 'NO'}

    def __init__(self,
                 member_name,
                 apply_ec4_min_shear: bool):
        self.member_name = member_name
        self.apply = self._apply_ec4_min_shear[apply_ec4_min_shear]


    def __repr__(self) -> str:
        return f"STUD_EC4_APPLY({self.apply})"

    def __str__(self) -> str:
        return f"STUD_EC4_APPLY,{self.member_name},{self.apply}"
