"""
Composy - Compos API python wrapper
Compos file definition - Final Restraint No Stud
"""
__all__ = ['FinalRestraintNoStud']


class FinalRestraintNoStud():
    _is_restraint = {True: 'NOSTUD_ZONE_LATERAL_FIXED',
                     False: 'NOSTUD_ZONE_LATERAL_FREE'}

    def __init__(self,
                 member_name,
                 is_nostud_fixed: bool):
        self.member_name = member_name
        self.restraint = self._is_restraint[is_nostud_fixed]

    def __repr__(self) -> str:
        return f"FINAL_RESTRAINT_NOSTUD({self.restraint})"

    def __str__(self) -> str:
        return f"FINAL_RESTRAINT_NOSTUD,{self.member_name},{self.restraint}"
