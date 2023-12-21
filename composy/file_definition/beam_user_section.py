"""
Composy - Compos API python wrapper
Compos file definition - Beam Steel Material User
"""
__all__ = ['BeamUserSection']


class BeamUserSection():
    def __init__(self,
                 member_name,
                 description: str):
        self.member_name = member_name
        self.description = description

    def __repr__(self) -> str:
        return f"BEAM_USER_SECTION({self.description})"

    def __str__(self) -> str:
        return f"BEAM_USER_SECTION,{self.member_name},{self.description}"
