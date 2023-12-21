"""
Composy - Compos API python wrapper
Compos file definition - Final Restraint Secondary Beam
"""
__all__ = ['FinalRestraintSecBeam']


class FinalRestraintSecBeam():
    _is_restraint = {True: '2ND_BEAM_AS_REST',
                     False: '2ND_BEAM_NOT_AS_REST'}

    def __init__(self,
                 member_name,
                 is_secondary_rest: bool):
        self.member_name = member_name
        self.restraint = self._is_restraint[is_secondary_rest]

    def __repr__(self) -> str:
        return f"FINAL_RESTRAINT_2ND BEAM({self.restraint})"

    def __str__(self) -> str:
        return f"FINAL_RESTRAINT_2ND BEAM,{self.member_name},{self.restraint}"
