"""
Composy - Compos API python wrapper
Compos file definition - Stud No Stud Zone
"""

__all__ = ['NoStudZone']


class NoStudZone:
    def __init__(self, member_name, left_end_pos: float, right_end_pos: float):
        self.member_name = member_name
        self.left_end_pos = left_end_pos
        self.right_end_pos = right_end_pos

    def __repr__(self) -> str:
        return f'STUD_NO_STUD_ZONE({self.left_end_pos},{self.right_end_pos})'

    def __str__(self) -> str:
        return f'STUD_NO_STUD_ZONE,{self.member_name},{self.left_end_pos},{self.right_end_pos}'
